import numpy as np
import torch

import sukta.tree_util as stu
from sukta.logging import n2str


def num_params(model: torch.nn.Module, requires_grad: bool = True):
    return n2str(
        sum(
            p.numel()
            for p in model.parameters()
            if (not requires_grad) or p.requires_grad
        )
    )


def clone(x):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: lambda v: v.clone(),
                np.ndarray: lambda v: v.copy(),
            },
            fallback=lambda v: v,
        ),
        x,
    )


def detach(x):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: lambda v: v.detach(),
            },
            fallback=lambda v: v,
        ),
        x,
    )


def detach_clone(x):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: lambda v: v.detach().clone(),
            },
            fallback=lambda v: v,
        ),
        x,
    )


def to_batch(x):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor | np.ndarray: lambda v: v[None, ...],
                type(None): lambda v: v,
            },
            fallback=lambda v: v,
        ),
        x,
    )


def to_device(x, device):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: lambda v, d=device: v.to(d),
                type(None): lambda v: v,
            },
        ),
        x,
    )


def to_tensor(x):
    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: lambda v: v,
                np.ndarray: torch.from_numpy,
                type(None): lambda v: v,
            }
        ),
        x,
    )


def itemize(x):
    def f(v):
        try:
            return v.item()
        except ValueError:
            return None

    d = stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: f,
                np.ndarray: f,
            },
            fallback=lambda v: None,
        ),
        x,
    )
    # prune none
    out = dict()
    for k, v in stu.iter_path(d):
        if v is not None:
            stu.dict_set_path(out, k, v)
    return out


def to_numpy(x):
    def f(tensor):
        if tensor.is_cuda:
            return tensor.detach().cpu().numpy()
        else:
            return tensor.detach().numpy()

    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: f,
                np.ndarray: lambda x: x,
                type(None): lambda x: x,
            },
        ),
        x,
        dict_type=dict | torch.nn.ParameterDict,
    )


def to_list(x):
    """
    Converts all torch tensors and numpy arrays in nested dictionary or list
    or tuple to a list, and returns a new nested structure. Useful for
    json encoding.

    Args:
        x (dict or list or tuple): a possibly nested dictionary or list or tuple

    Returns:
        y (dict or list or tuple): new nested dict-list-tuple
    """

    def f(tensor):
        if tensor.is_cuda:
            return tensor.detach().cpu().numpy().tolist()
        else:
            return tensor.detach().numpy().tolist()

    return stu.apply_vfunc(
        stu.type_cond_func(
            {
                torch.Tensor: f,
                np.ndarray: lambda x: x.tolist(),
                type(None): lambda x: x,
            },
        ),
        x,
    )
