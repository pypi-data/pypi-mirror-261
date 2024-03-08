import numpy as np

from sukta.torch.module.normalizer import SingleFieldLinearNormalizer


def get_range_normalizer_from_stat(stat, output_max=1, output_min=-1, range_eps=1e-7):
    # -1, 1 normalization
    input_max = stat["max"]
    input_min = stat["min"]
    input_range = input_max - input_min
    ignore_dim = input_range < range_eps
    input_range[ignore_dim] = output_max - output_min
    scale = (output_max - output_min) / input_range
    offset = output_min - scale * input_min
    offset[ignore_dim] = (output_max + output_min) / 2 - input_min[ignore_dim]

    return SingleFieldLinearNormalizer.create_manual(
        scale=scale, offset=offset, input_stats_dict=stat
    )


def get_image_range_normalizer():
    scale = np.array([2], dtype=np.float32)
    offset = np.array([-1], dtype=np.float32)
    stat = {
        "min": np.array([0], dtype=np.float32),
        "max": np.array([1], dtype=np.float32),
        "mean": np.array([0.5], dtype=np.float32),
        "std": np.array([np.sqrt(1 / 12)], dtype=np.float32),
    }
    return SingleFieldLinearNormalizer.create_manual(
        scale=scale, offset=offset, input_stats_dict=stat
    )


def get_image_unit_normalizer(v_min=0, v_max=255):
    assert v_max > v_min
    s = 1 / (v_max - v_min)
    scale = np.array([s], dtype=np.float32)
    offset = np.array([-v_min * s], dtype=np.float32)
    stat = {
        "min": np.array([v_min], dtype=np.float32),
        "max": np.array([v_max], dtype=np.float32),
        "mean": np.array([(v_max - v_min) / 2], dtype=np.float32),
        "std": np.array([(v_max - v_min) * np.sqrt(1 / 12)], dtype=np.float32),
    }
    return SingleFieldLinearNormalizer.create_manual(
        scale=scale, offset=offset, input_stats_dict=stat
    )


def get_image_identity_normalizer():
    return get_image_unit_normalizer(v_min=0, v_max=1)


def get_gaussian_normalizer_from_stat(stat, std_eps=1e-4):
    input_mean = stat["mean"]
    input_std = stat["std"]
    ignore_dim = input_std < std_eps
    input_std[ignore_dim] = 1.0
    scale = 1.0 / input_std
    offset = -scale * input_mean

    return SingleFieldLinearNormalizer.create_manual(
        scale=scale, offset=offset, input_stats_dict=stat
    )


def get_identity_normalizer_from_stat(stat):
    scale = np.ones_like(stat["min"])
    offset = np.zeros_like(stat["min"])
    return SingleFieldLinearNormalizer.create_manual(
        scale=scale, offset=offset, input_stats_dict=stat
    )


def array_to_stats(arr: np.ndarray):
    stat = {
        "min": np.min(arr, axis=0),
        "max": np.max(arr, axis=0),
        "mean": np.mean(arr, axis=0),
        "std": np.std(arr, axis=0),
    }
    return stat
