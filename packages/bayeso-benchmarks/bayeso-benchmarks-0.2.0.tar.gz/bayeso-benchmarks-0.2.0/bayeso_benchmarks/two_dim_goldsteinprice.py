#
# author: Jungtaek Kim (jungtaek.kim.mail@gmail.com)
# last updated: August 4, 2023
#

import numpy as np

from bayeso_benchmarks.benchmark_base import Function


def fun_target(bx, dim_bx):
    assert len(bx.shape) == 1
    assert bx.shape[0] == dim_bx

    term_1a = (bx[0] + bx[1] + 1.0)**2
    term_1b = 19.0 - 14.0 * bx[0] + 3.0 * bx[0]**2 - 14.0 * bx[1] + 6.0 * bx[0] * bx[1] + 3.0 * bx[1]**2
    term_1 = 1.0 + term_1a * term_1b

    term_2a = (2.0 * bx[0] - 3.0 * bx[1])**2
    term_2b = 18.0 - 32.0 * bx[0] + 12.0 * bx[0]**2 + 48.0 * bx[1] - 36.0 * bx[0] * bx[1] + 27.0 * bx[1]**2
    term_2 = 30.0 + term_2a * term_2b

    y = term_1 * term_2
    return y


class GoldsteinPrice(Function):
    def __init__(self, seed=None):
        assert isinstance(seed, (type(None), int))

        dim_bx = 2
        bounds = np.array([
            [-2.0, 2.0],
            [-2.0, 2.0],
        ])
        assert bounds.shape[0] == dim_bx
        assert bounds.shape[1] == 2

        global_minimizers = np.array([
            [0.0, -1.0],
        ])
        global_minimum = 2.9999999999
        function = lambda bx: fun_target(bx, dim_bx)

        super().__init__(dim_bx, bounds, global_minimizers, global_minimum, function, seed=seed)
