#
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: December 4, 2022
#

import numpy as np
import pytest

from bayeso_benchmarks.inf_dim_ackley import *

class_fun = Ackley
str_name = 'ackley'

TEST_EPSILON = 1e-5


def test_init():
    obj_fun = class_fun(2)

    with pytest.raises(TypeError) as error:
        class_fun()
    with pytest.raises(AssertionError) as error:
        class_fun('abc')
    with pytest.raises(AssertionError) as error:
        class_fun(2.1)
    with pytest.raises(AssertionError) as error:
        class_fun(2, seed='abc')
    with pytest.raises(AssertionError) as error:
        class_fun(2, seed=2.1)

def test_validate_properties():
    obj_fun = class_fun(5)
    obj_fun.validate_properties()

def test_output():
    obj_fun = class_fun(3)
    bounds = obj_fun.get_bounds()

    grids = obj_fun.sample_grids(3)
    truths_grids = np.array([
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [4.44089210e-16],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
    ])
    
    print(grids)
    print(obj_fun.output(grids))
    print(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)
    assert np.all(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)

def test_call():
    obj_fun = class_fun(3)
    bounds = obj_fun.get_bounds()

    grids = obj_fun.sample_grids(3)
    truths_grids = np.array([
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [4.44089210e-16],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.02411230e+01],
        [2.11187470e+01],
        [2.15703112e+01],
        [2.11187470e+01],
        [2.15703112e+01],
    ])
    
    print(grids)
    print(obj_fun(grids))
    print(np.abs(obj_fun(grids) - truths_grids) < TEST_EPSILON)
    assert np.all(np.abs(obj_fun(grids) - truths_grids) < TEST_EPSILON)

def test_name():
    obj_fun = class_fun(2)
    assert obj_fun.name == str_name + '_2'

    obj_fun = class_fun(4)
    assert obj_fun.name == str_name + '_4'

    obj_fun = class_fun(16)
    assert obj_fun.name == str_name + '_16'

    assert obj_fun.__class__.__name__.lower() == str_name
    assert obj_fun.__class__.__qualname__.lower() == str_name
