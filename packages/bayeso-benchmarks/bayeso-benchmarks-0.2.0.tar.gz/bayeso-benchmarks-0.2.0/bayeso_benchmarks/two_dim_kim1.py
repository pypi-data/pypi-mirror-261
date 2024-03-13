#
# author: Jungtaek Kim (jungtaek.kim.mail@gmail.com)
# last updated: August 4, 2023
#

import numpy as np

from bayeso_benchmarks.benchmark_base import Function


def fun_target(bx, dim_bx):
    assert len(bx.shape) == 1
    assert bx.shape[0] == dim_bx

    y = np.sin(bx[0]) + np.cos(bx[1]) + 0.016 * (bx[0] - 5.0)**2 + 0.008 * (bx[1] - 5.0)**2
    return y


class Kim1(Function):
    def __init__(self, seed=None):
        assert isinstance(seed, (type(None), int))

        dim_bx = 2
        bounds = np.array([
            [-16.0, 16.0],
            [-16.0, 16.0],
        ])
        assert bounds.shape[0] == dim_bx
        assert bounds.shape[1] == 2

        global_minimizers = np.array([
            [4.72130726, 3.17086303],
        ])
        global_minimum = -1.9715232348
        function = lambda bx: fun_target(bx, dim_bx)

        super().__init__(dim_bx, bounds, global_minimizers, global_minimum, function, seed=seed)
