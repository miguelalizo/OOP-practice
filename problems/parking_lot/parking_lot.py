"""
Constraints and Assumptions

Types of cars supported:
- motorcycle
- car
- bus

Does each vehicle take up a different amount of parking spots?
- Yes

Are there multiple types of parking spots?
- Yes
- Motorcycle Spot -> Motorcycle
- Compact spot -> Motorcycle + car
- Large spot -> Motorcycle + Car
- Bus takes 5 large parking spots

Does the parking lot have multiple levels
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Self


class SpotSize(Enum):
    """
    Enumeration of the supported spot sizes
    """

    Motorcycle = 0
    Compact = 1
    Large = 2
    Bus = 3


class SpotStatus(Enum):
    """
    Enumeration of the spot status
    """

    Vacant = 0
    Taken = 1
    Reserved = 2


class Spot:
    """
    Class that defines a spot
    """

    def __init__(self, spot_size: SpotSize):
        self.spot_size = spot_size
        self.status: SpotStatus = SpotStatus.Vacant
        self.reserved_by: str = None

    def is_available(self) -> bool:
        return self.status == SpotStatus.Vacant

    def take_spot(self) -> None:
        self.status = SpotStatus.Taken

    def reserve_spot(self, name: str) -> None:
        self.status = SpotStatus.Taken
        self.reserved_by = name

    def clear_spot(self) -> None:
        self.status = SpotStatus.Vacant
        self.reserved_by = None


class Vehicle(ABC):
    """
    Vehicle Abstract Class
    """

    def __init__(self, spot_size: SpotSize, owner: str, plate: str, spots_needed: int):
        self.spot_size = spot_size
        self.owner = owner
        self.plate = plate
        self.spots_needed = spots_needed
        self.spots: List[Spot] = []

    @abstractmethod
    def can_fit_in_spot(self, spot: Spot):
        pass

    def clear_spots(self) -> None:
        for spot in self.spots:
            spot.clear_spot()

    def take_spot(self, spot: Spot) -> None:
        self.spots.append(spot)
        spot.take_spot()


class Motorcycle(Vehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Motorcycle, owner, plate, 1)

    def can_fit_in_spot(self, spot: Spot):
        return spot.is_available()


class Compact(Vehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Compact, owner, plate, 1)

    def can_fit_in_spot(self, spot: Spot):
        return (
            spot.spot_size == SpotSize.Compact
            or spot.spot_size == SpotSize.Large
            and spot.is_available()
        )


class LargeCar(Vehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Large, owner, plate, 1)

    def can_fit_in_spot(self, spot: Spot):
        return spot.spot_size == SpotSize.Large and spot.is_available()


class Bus(Vehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Bus, owner, plate, 5)

    def can_fit_in_spot(self, spot: Spot):
        return spot.spot_size == SpotSize.Large and spot.is_available()


class FloorBuilder:
    def __init__(self):
        self.spots: List[Spot] = []

    def _add_spots(self, spot_size: SpotSize, amount: int):
        for _ in range(amount):
            spot = Spot(spot_size)
            self.spots.append(spot)
        return self

    def add_motorcycle_spots(self, amount: int) -> Self:
        self._add_spots(SpotSize.Motorcycle, amount)
        return self

    def add_compact_spots(self, amount: int) -> Self:
        self._add_spots(SpotSize.Compact, amount)
        return self

    def add_large_spots(self, amount: int) -> Self:
        self._add_spots(SpotSize.Large, amount)
        return self

    def add_bus_spots(self, amount: int) -> Self:
        self._add_spots(SpotSize.Large, 5 * amount)
        return self

    def finalize(self) -> Floor:
        if not self.spots:
            raise Exception("floor must have at least 1 spot")
        return Floor(self.spots)


class Floor:
    def __init__(self, spots: List[Spot]):
        self.spots: List[Spot] = spots

    @staticmethod
    def build():
        return FloorBuilder()

    def available_spots(self) -> int:
        res = 0
        for spot in self.spots:
            if spot.status == SpotStatus.Vacant:
                res += 1
        return res

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        count = 0
        spots = []
        for spot in self.spots:
            if vehicle.can_fit_in_spot(spot):
                count += 1
                spots.append(spot)
                if count == vehicle.spots_needed:
                    for s in spots:
                        vehicle.take_spot(s)
                    return True
            else:
                count = 0
                spots = []
        return False


class ParkingLot:
    def __init__(self, floors: List[Floor] = None):
        self.floors: List[Floor] = floors

    def add_floor(self, floor: Floor) -> None:
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            if floor.park_vehicle(vehicle) is True:
                print(f"vehicle: {vehicle.spot_size}-{vehicle.plate} parked")
                return True
        print(f"No spots available for vehicle: {vehicle.spot_size}-{vehicle.plate}")
        return False

    def vacate_spot(self, vehicle: Vehicle):
        vehicle.clear_spots()


def main():
    floor1 = (
        Floor.build()
        .add_motorcycle_spots(10)
        .add_compact_spots(1)
        .add_large_spots(5)
        .add_bus_spots(2)
        .finalize()
    )

    floor2 = (
        Floor.build()
        .add_motorcycle_spots(10)
        .add_compact_spots(10)
        .add_large_spots(10)
        .add_bus_spots(2)
        .finalize()
    )

    lot = ParkingLot([floor1, floor2])

    car1 = LargeCar("owner1", "AB123")
    bus1 = Bus("busowner", "busplate")

    lot.park_vehicle(car1)
    lot.park_vehicle(bus1)

    for spot in bus1.spots:
        print(spot.status)

    lot.vacate_spot(bus1)

    for spot in bus1.spots:
        print(spot.status)


if __name__ == "__main__":
    main()
