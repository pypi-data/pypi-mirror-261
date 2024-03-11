import glob
import logging
import math
import random
import signal
import sys
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, Literal, Optional

import numpy as np

import sukta.tree_util as stu
from sukta.logging import getLogger, n2str, str2n
from sukta.metrics import TrackerConfig


@dataclass
class CheckpointConfig:
    top_k: int = 1
    mode: Literal["min", "max"] = "min"
    metric_key: str = "loss"

    save_dir: Path = field(init=False)
    ckpt_path_map: Dict[str, float] = field(init=False, default_factory=dict)
    default_value: float = field(init=False)

    def __post_init__(self):
        if self.mode == "min":
            self.default_value = math.inf
        else:
            self.default_value = -math.inf

    def get_ckpt_path(
        self,
        step: int | None = None,
        epoch: int | None = None,
        metric: float | None = None,
    ) -> Optional[Path]:
        if self.top_k == 0:
            return None
        ckpt_name = f'ts={datetime.now().strftime("%Y%m%d_%H%M%S")}'
        if step is not None:
            ckpt_name += f"_step={step:d}"
        elif epoch is not None:
            ckpt_name += f"_epoch={epoch:d}"
        ckpt_name += (
            f'_{self.metric_key}={n2str(metric, fmt=".3f")}'
            if metric is not None
            else ""
        )
        ckpt_name += ".ckpt"
        ckpt_path = self.save_dir / ckpt_name

        if self.top_k < 0 or len(self.ckpt_path_map) < self.top_k:
            # under-capacity
            self.ckpt_path_map[ckpt_path] = metric or self.default_value
            return ckpt_path

        # at capacity
        sorted_map = sorted(self.ckpt_path_map.items(), key=lambda x: x[1])
        min_path, min_value = sorted_map[0]
        max_path, max_value = sorted_map[-1]

        delete_path: Path = None
        if self.mode == "max":
            if metric >= min_value:
                delete_path = min_path
        else:
            if metric <= max_value:
                delete_path = max_path

        if delete_path is None:
            return None
        else:
            del self.ckpt_path_map[delete_path]
            self.ckpt_path_map[ckpt_path] = metric or self.default_value
            delete_path.unlink(missing_ok=True)
            return ckpt_path

    def get_best_ckpt(self):
        if not self.ckpt_path_map:
            return None
        sorted_map = sorted(self.ckpt_path_map.items(), key=lambda x: x[1])
        min_path = sorted_map[0][0]
        max_path = sorted_map[-1][0]

        if self.mode == "max":
            return max_path
        else:
            return min_path


@dataclass
class WorkspaceConfig:
    experiment: str = "default"

    tracker: TrackerConfig = field(default_factory=TrackerConfig)
    ckpt: CheckpointConfig = field(default_factory=CheckpointConfig)
    log: logging.Logger = field(init=False)

    seed: int = 0
    run_dir: Path | None = None
    resume_from: Literal["latest", "best"] = "latest"

    def __post_init__(self):
        if self.run_dir is None:
            self.run_dir = (
                Path("runs")
                / f'{self.experiment}_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            )
        self.run_dir.mkdir(exist_ok=True, parents=True)
        self.ckpt.save_dir = self.run_dir / "checkpoints"
        self.ckpt.save_dir.mkdir(exist_ok=True)
        self.ckpt.ckpt_path_map = {
            Path(p): str2n(p.split(self.ckpt.metric_key + "=")[-1].split(".ckpt")[0])
            for p in glob.glob(str(self.ckpt.save_dir / "ts=*.ckpt"))
        }
        log_dir = self.run_dir / "logs"
        log_dir.mkdir(exist_ok=True)
        self.log = getLogger(self.experiment, log_dir)
        self.tracker.replace(
            experiment=self.experiment,
            logger=self.log,
            log_dir=log_dir,
        )

    @property
    def hparam_dict(self):
        hdict = asdict(self)
        del hdict["log"]
        del hdict["tracker"]
        del hdict["ckpt"]
        del hdict["resume_from"]
        return {
            k: v
            for k, v in stu.iter_path(
                stu.apply_vfunc(
                    stu.type_cond_func(
                        {
                            bool: bool,
                            int: int,
                            float: float,
                        },
                        fallback=str,
                    ),
                    hdict,
                ),
                delim="/",
            )
        }


class Workspace(ABC):
    include_keys = tuple()
    exclude_keys = tuple()

    def __init__(self, cfg: WorkspaceConfig):
        signal.signal(signal.SIGINT, self.handle_stop_signals)
        signal.signal(signal.SIGTERM, self.handle_stop_signals)

        self.cfg = cfg
        self.log = cfg.log
        self.tracker = None
        self._saving_thread = None
        self.set_seed(cfg.seed)

    def __call__(self):
        # try restoring the latest checkpoint
        if self.cfg.resume_from == "latest":
            self.load_checkpoint(tag="latest")
        else:
            ckpt_path = self.cfg.ckpt.get_best_ckpt()
            if ckpt_path is not None:
                self.load_checkpoint(ckpt_path)
        # run with trackers initialized
        with self.cfg.tracker.get_tracker() as self.tracker:
            try:
                self.run()
            finally:
                self.finish()

    @abstractmethod
    def run(self):
        """
        TIPS:
        - self exposes `log` and `tracker` for IO logging and metrics
        - add hparam logging at the beginning of main

            ```python
            tracker.hparams(self.cfg.hparam_dict, key_metrics=['loss'])
            ```
        """

    def set_seed(self, seed):
        np.random.seed(seed)
        random.seed(seed)

    def save_snapshot(self, tag: str = "latest") -> str:
        raise NotImplementedError()

    @classmethod
    def create_from_snapshot(cls, path: Path):
        raise NotImplementedError()

    @abstractmethod
    def save_checkpoint(
        self, path: Path = None, tag: str = "latest", use_thread: bool = True
    ) -> str: ...

    @abstractmethod
    def load_checkpoint(self, path: Path = None, tag: str = "latest", **kwargs): ...

    @classmethod
    @abstractmethod
    def create_from_checkpoint(cls, path: Path, **kwargs): ...

    def finish(self):
        self.save_checkpoint(use_thread=False)

    def handle_stop_signals(self, signum, frame):
        self.log.warning("SIGINT or SIGTERM received")
        sys.exit(0)
