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
    def build() -> IHouse:
        """Implement in child class"""


class RegularHouseBuilder(IHouseBuilder):
    def __init__(self):
        self.roof = None
        self.kitchen = None
        self.garage = None
        self.rooms = []

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

    def build(self) -> RegularHouse:
        if not self.roof:
            raise Exception("House creation error: House must contain a roof")
        if not self.kitchen:
            raise Exception("House creation error: House must contain a kitchen")
        if not self.rooms:
            raise Exception(
                "House creation error: House must contain at least one room"
            )
        return RegularHouse(
            roof=self.roof,
            kitchen=self.kitchen,
            rooms=self.rooms,
            garage=self.garage,
        )


class RegularHouse(IHouse):
    def __init__(self, roof=None, kitchen=None, rooms=None, garage=None):
        self.roof = roof
        self.kitchen = kitchen
        self.rooms = rooms
        self.garage = garage

    def print_house(self):
        print(f"Roof: {self.roof}\nKitchen: {self.kitchen}\nRooms: {self.rooms}\n")

    @staticmethod
    def build_house() -> RegularHouseBuilder:
        return RegularHouseBuilder()


class HouseWithPoolBuilder(IHouseBuilder):
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

    def build(self) -> HouseWithPool:
        if not self.roof:
            raise Exception("House creation error: HouseWithPool must contain a roof")
        if not self.kitchen:
            raise Exception(
                "House creation error: HouseWithPool must contain a kitchen"
            )
        if not self.rooms:
            raise Exception(
                "House creation error: HouseWithPool must contain at least one room"
            )
        if not self.pool:
            raise Exception("House creation error: HouseWithPool must contain a a pool")
        return HouseWithPool(
            roof=self.roof,
            kitchen=self.kitchen,
            rooms=self.rooms,
            garage=self.garage,
            pool=self.pool,
        )


class HouseWithPool(IHouse):
    def __init__(self, roof=None, kitchen=None, rooms=None, garage=None, pool=None):
        self.roof = roof
        self.kitchen = kitchen
        self.rooms = rooms
        self.garage = garage
        self.pool = pool

    def print_house(self):
        print(
            f"Roof: {self.roof}\nKitchen: {self.kitchen}"
            f"\nRooms: {self.rooms}\nPool: {self.pool}"
        )

    @staticmethod
    def build_house() -> HouseWithPoolBuilder:
        return HouseWithPoolBuilder()


if __name__ == "__main__":
    reg_house = (
        RegularHouse.build_house()
        .add_roof("A-frame")
        .add_kitchen("kitchen with island")
        .add_room("living-room")
        .add_room("bedroom-1")
        .add_room("bedroom-2")
        .add_room("bedroom-3")
        .build()
    )

    reg_house.print_house()

    house_with_pool = (
        HouseWithPool.build_house()
        .add_roof("A-frame")
        .add_kitchen("kitchen with island")
        .add_room("living-room")
        .add_room("bedroom-1")
        .add_room("bedroom-2")
        .add_room("bedroom-3")
        .add_pool("round-pool")
        .build()
    )

    house_with_pool.print_house()
