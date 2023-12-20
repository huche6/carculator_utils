"""Load a driving cycle based on the name specified by the user.

The driving cycle returned is a numpy
array with speed levels (in km/h) for each
second of driving.
"""
from pathlib import Path
from typing import List, Tuple

import numpy as np
import yaml

from carculator_utils import data as data_carculator
from carculator_utils import get_data

def detect_vehicle_type(vehicle_sizes: List[str]) -> str:
    """Detect the type of vehicle based on the size of the vehicle."""

    dc = get_driving_cycle_specs()

    for vehicle_type in dc["columns"]:
        for dc_name in dc["columns"][vehicle_type]:
            for size in dc["columns"][vehicle_type][dc_name]:
                if size in vehicle_sizes:
                    return vehicle_type

    raise ValueError("The vehicle size is not in the list of available vehicle sizes.")


def get_driving_cycle_specs() -> dict:
    """Get driving cycle specifications.

    :returns: A dictionary with driving cycle specifications.
    :rtype: dict

    """

    with open(Path(data_carculator.__file__).parent / "driving cycle" / "dc_specs.yaml", "r") as f:
        return yaml.safe_load(f)


def get_standard_driving_cycle_and_gradient(
    vehicle_type: str, vehicle_sizes: List[str], name: str
) -> Tuple[np.ndarray, np.ndarray]:
    """Get driving cycle and gradient data as a Pandas `Series`.

    Driving cycles are given as km/h per second up to 3200 seconds.

    :param name: The name of the driving cycle.
    e.g., WLTC (Worldwide harmonized Light vehicles Test Cycles)
    :type name: str

    :returns: A pandas DataFrame object with driving time
    (in seconds) as index, and velocity (in km/h) as values.
    :rtype: panda.Series

    """

    filepath_dc = Path(data_carculator.__file__).parent / "driving cycle" / f"{vehicle_type}.csv"
    filepath_gradient = Path(data_carculator.__file__).parent / "gradient" / f"{vehicle_type}.csv"

    # definition of columns to select in the CSV file
    # each column corresponds to a size class
    # since the driving cycle is simulated for each size class
    return (
        get_data(filepath_dc, vehicle_type, vehicle_sizes, name),
        get_data(filepath_gradient, vehicle_type, vehicle_sizes, name),
    )
