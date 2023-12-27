import pytest
from xarray import DataArray
import numpy as np

from carculator_utils import (
    isarray,
    replace_values_in_array,
)


class TestDataManagement:
    def test_isarray(self):
        x = [1, 2, 3]
        assert isinstance(isarray(x), np.ndarray)

    @pytest.mark.parametrize(
        "x, cond",
        [
            (np.array([1, 0, 1, np.nan, 1]), lambda x: (x == 0) | np.isnan(x)),
            (np.array([1, 1, 0, 1, 0]), lambda x: x == 0),
            (np.array([0, 0.1, 0.5, 1, 0.8]), lambda x: x < 1),
        ],
    )
    def test_replace_values_in_array(self, x, cond):
        np.testing.assert_array_equal(
            replace_values_in_array(x, cond), np.array([1, 1, 1, 1, 1])
        )
