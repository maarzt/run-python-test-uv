
from run_python_test_uv.foo import *
import numpy as np

def test_foo():
    assert np.array_equal(return1234(), np.array([1, 2, 3, 4]))