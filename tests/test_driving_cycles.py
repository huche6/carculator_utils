from carculator_utils.driving_cycles import detect_vehicle_type, get_driving_cycle_specs
import pytest


class TestDrivingCycleFunctions:
    @pytest.mark.parametrize(
        "two_wheeler_types",
        list(
            (
                get_driving_cycle_specs()["columns"]["two-wheeler"]["Two wheeler cycle"]
            ).keys()
        ),
    )
    def test_vehicle_type_two_wheeler(self, two_wheeler_types):
        assert detect_vehicle_type(two_wheeler_types) == "two-wheeler"

    @pytest.mark.parametrize(
        "car_driving_types",
        list(list(get_driving_cycle_specs()["columns"]["car"].values())[0].keys()),
    )
    def test_vehicle_type_two_wheeler(self, car_driving_types):
        assert detect_vehicle_type(car_driving_types) == "car"

    @pytest.mark.parametrize(
        "truck_driving_types",
        list(list(get_driving_cycle_specs()["columns"]["truck"].values())[0].keys()),
    )
    def test_vehicle_type_truck(self, truck_driving_types):
        assert detect_vehicle_type(truck_driving_types) == "truck"

    @pytest.mark.parametrize(
        "bus_driving_types",
        list((get_driving_cycle_specs()["columns"]["bus"]["bus"]).keys()),
    )
    def test_vehicle_type_bus(self, bus_driving_types):
        assert detect_vehicle_type(bus_driving_types) == "bus"
