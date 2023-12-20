from typing import List
from carculator_utils import get_driving_cycle_specs

def get_dc_column_number(vehicle_type: str, vehicle_size: List[str], dc_name: str) -> List[int]:
    """Load YAML file that contains the column number.

    Return the column number given a vehicle type and driving cycle name.
    """

    dc_specs = get_driving_cycle_specs()

    if isinstance(vehicle_size, str):
        vehicle_size = [vehicle_size]

    if vehicle_type not in dc_specs["columns"]:
        raise KeyError(
            f"Vehicle type {vehicle_type} is not in the list of "
            f"available vehicle types: {list(dc_specs['columns'].keys())}"
        )

    if dc_name not in dc_specs["columns"][vehicle_type]:
        raise KeyError(
            f"Driving cycle {dc_name} is not in the list of "
            f"available driving cycles: {list(dc_specs['columns'][vehicle_type].keys())}"
        )

    if not all(vehicle in dc_specs["columns"][vehicle_type][dc_name] for vehicle in vehicle_size):
        raise KeyError(
            f"Vehicle size(s) {vehicle_size} is not in the list of "
            f"available vehicle sizes: {list(dc_specs['columns'][vehicle_type][dc_name].keys())}"
        )

    return [dc_specs["columns"][vehicle_type][dc_name][s] for s in vehicle_size]