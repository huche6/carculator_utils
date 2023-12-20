import numpy as np
from pathlib import Path
from typing import List
from carculator_utils import get_dc_column_number

def get_data(filepath: Path, vehicle_type: str, vehicle_sizes: List[str], name: str) -> np.ndarray:
    """Get data of a specified cycle."""

    try:
        col = get_dc_column_number(vehicle_type, vehicle_sizes, name)
        arr = np.genfromtxt(filepath, delimiter=";")
        # we skip the headers
        dc = arr[1:, col]
        return dc

    except KeyError as err:
        print(err, "The specified driving cycle could not be found.")
        raise