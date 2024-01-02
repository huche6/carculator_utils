import json
import os
from pathlib import Path

import numpy as np
import pytest

from carculator_utils import data_to_dict, isarray, load_parameters, replace_values_in_array


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
        np.testing.assert_array_equal(replace_values_in_array(x, cond), np.array([1, 1, 1, 1, 1]))

    def test_load_parameters_with_valid_filepath(self):
        temp_file_path = "test_parameters.json"
        test_data = {"param1": 1, "param2": "value"}
        with open(temp_file_path, "w") as temp_file:
            json.dump(test_data, temp_file)

        result = load_parameters(temp_file_path)
        expected_result = test_data
        print(expected_result)
        assert result == expected_result

        os.remove("test_parameters.json")
        assert not Path(temp_file_path).exists()

    def test_load_parameters_with_invalid_filepath(self):
        invalid_file_path = "nonexistent_file.json"
        with pytest.raises(AssertionError) as context:
            load_parameters(invalid_file_path)
        assert "Can't find this filepath" in str(context.value)

    def test_load_parameters_with_non_filepath(self):
        input_parameters = {"param1": 1, "param2": "value"}
        result = load_parameters(input_parameters)
        expected_result = input_parameters
        assert result == expected_result

    def test_data_to_dict(self):
        csv_list = [
            ["ID", "Name", "Age"],
            ["1", "John", "25"],
            ["2", "Jane", "30"],
            ["3", "Doe", "40"],
        ]

        result = data_to_dict(csv_list)

        assert result == {
            "1": {"Name": "John", "Age": "25"},
            "2": {"Name": "Jane", "Age": "30"},
            "3": {"Name": "Doe", "Age": "40"},
        }

    def test_data_to_dict_empty_list(self):
        csv_list = []

        result = data_to_dict(csv_list)

        assert result == {}

    def test_data_to_dict_different_lengths(self):
        csv_list = [
            ["ID", "Name", "Age"],
            ["1", "John"],
            ["2", "Jane", "30"],
        ]

        result = data_to_dict(csv_list)

        assert result == {
            "1": {"Name": "John"},
            "2": {"Name": "Jane", "Age": "30"},
        }
