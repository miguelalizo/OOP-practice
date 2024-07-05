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


class IVehicle(ABC):
    """
    Vehicle Abstract Class
    """

    def __init__(self, spot_size: SpotSize, owner: str, plate: str):
        self.spot_size = spot_size
        self.owner = owner
        self.plate = plate

    @abstractmethod
    def can_fit_in_spot(self, spot: Spot):
        pass


class Motorcycle(IVehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Motorcycle, owner, plate)

    def can_fit_in_spot(self, spot: Spot):
        return True


class Compact(IVehicle):
    def __init__(self, vehicle_type: SpotSize, owner: str, plate: str):
        super().__init__(SpotSize.Compact, owner, plate)

    def can_fit_in_spot(self, spot: Spot):
        return spot.spot_size == SpotSize.Compact or spot.spot_size == SpotSize.Large


class LargeCar(IVehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Large, owner, plate)

    def can_fit_in_spot(self, spot: Spot):
        return spot.spot_size == SpotSize.Large


class Bus(IVehicle):
    def __init__(self, owner: str, plate: str):
        super().__init__(SpotSize.Bus, owner, plate)

    def can_fit_in_spot(self, spot: Spot):
        return spot.spot_size == SpotSize.Large


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

    def park_vehicle(self, vehicle: IVehicle) -> bool:
        count = 0
        spots = []
        for spot in self.spots:
            if vehicle.can_fit_in_spot(spot) and spot.is_available():
                count += 1
                spots.append(spot)
                if vehicle.spot_size != SpotSize.Bus or (
                    vehicle.spot_size == SpotSize.Bus and count == 5
                ):
                    for s in spots:
                        s.take_spot()
                    return True
            else:
                count = 0
                spots = []
        return False


class ParkingLot:
    def __init__(self):
        self.floors: List[Floor] = []

    def add_floor(self, floor: Floor) -> None:
        self.floors.append(floor)

    def park_vehicle(self, vehicle: IVehicle):
        for floor in self.floors:
            if floor.park_vehicle(vehicle) is True:
                print(f"vehicle: {vehicle.spot_size}-{vehicle.plate} parked")
                return True
        print(f"No spots available for vehicle: {vehicle.spot_size}-{vehicle.plate}")
        return False


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

    lot = ParkingLot()
    lot.add_floor(floor1)
    lot.add_floor(floor2)

    car1 = LargeCar("owner1", "AB123")
    bus1 = Bus("busowner", "busplate")

    lot.park_vehicle(car1)
    lot.park_vehicle(bus1)


if __name__ == "__main__":
    main()
