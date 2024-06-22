from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Self


class IHouse(ABC):
    @abstractmethod
    def print_house():
        """Implement in child class"""


class IHouseBuilder(ABC):
    @abstractmethod
    def add_roof() -> IHouseBuilder:
        """Implement in child class"""

    @abstractmethod
    def add_kitchen() -> IHouseBuilder:
        """Implement in child class"""

    @abstractmethod
    def add_room() -> IHouseBuilder:
        """Implement in child class"""

    @abstractmethod
    def finalize() -> IHouse:
        """Implement in child class"""


class House(IHouse):
    def __init__(self):
        self.roof = None
        self.kitchen = None
        self.rooms = None
        self.garage = None
        self.pool = None

    def print_house(self):
        print(
            f"Roof: {self.roof}\nKitchen: {self.kitchen}"
            f"\nRooms: {self.rooms}\nPool: {self.pool}"
        )

    @staticmethod
    def build() -> HouseBuilder:
        return HouseBuilder()


class HouseBuilder(IHouseBuilder):
    def __init__(self):
        self.roof = None
        self.kitchen = None
        self.rooms = []
        self.garage = None
        self.pool = None

    def add_roof(self, roof: str) -> Self:
        if self.roof:
            raise Exception("House creation error: House already contains a roof")
        self.roof = roof
        return self

    def add_kitchen(self, kitchen: str) -> Self:
        if self.kitchen:
            raise Exception("House creation error: House already contains a kitchen")
        self.kitchen = kitchen
        return self

    def add_room(self, room: str) -> Self:
        self.rooms.append(room)
        return self

    def add_garage(self, garage: str) -> Self:
        self.garage = garage
        return self

    def add_pool(self, pool: str) -> Self:
        self.pool = pool
        return self

    def finalize(self) -> House:
        if not self.roof:
            raise Exception("House creation error: House must contain a roof")
        if not self.kitchen:
            raise Exception("House creation error: House must contain a kitchen")
        if not self.rooms:
            raise Exception(
                "House creation error: House must contain at least one room"
            )

        house = House()
        house.roof = self.roof
        house.kitchen = self.kitchen
        house.rooms = self.rooms
        house.garage = self.garage
        house.pool = self.pool

        self._clear()

        return house

    def _clear(self):
        """Clear all attributes of the HouseBuilder so it can be reused"""
        self.roof = None
        self.kitchen = None
        self.rooms = None
        self.garage = None
        self.pool = None


if __name__ == "__main__":
    reg_house = (
        House.build()
        .add_roof("A-frame")
        .add_kitchen("kitchen with island")
        .add_room("living-room")
        .add_room("bedroom-1")
        .add_room("bedroom-2")
        .add_room("bedroom-3")
        .finalize()
    )

    reg_house.print_house()

    house_with_pool = (
        House.build()
        .add_roof("A-frame")
        .add_kitchen("kitchen with island")
        .add_room("living-room")
        .add_room("bedroom-1")
        .add_room("bedroom-2")
        .add_room("bedroom-3")
        .add_pool("round-pool")
        .finalize()
    )

    house_with_pool.print_house()
