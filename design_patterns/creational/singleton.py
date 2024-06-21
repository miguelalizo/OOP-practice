from abc import ABC, abstractmethod
from typing import Union

FloatInt = Union[float, int]


class IPerson(ABC):
    """Person Interface"""

    @abstractmethod
    def get_data(self):
        """Implement in child class"""


class PersonSingleton(IPerson):
    """Implementation of the IPerson interface"""

    __instance = None

    def __init__(self, name, age):
        """
        Raises exception if instance is already present.

        It is safer to use PersonSingleton.get_instance() which will return the current
        instance if present, else it will create a new default instance and return it.
        """
        if PersonSingleton.__instance:
            raise Exception("PersonSingleton can only be instantiated once.")

        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    @staticmethod
    def get_instance():
        """
        Returns existing PersonSingleton instance if one exists. Otherwise it will
        create a default one and return it.
        """
        if not PersonSingleton.__instance:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def get_data(self) -> tuple[FloatInt, str]:
        """
        Returns name and age
        """
        return (self.age, self.name)


if __name__ == "__main__":
    s1 = PersonSingleton("myname", 1)
    s2 = PersonSingleton.get_instance()

    assert s2 is s1
    print(s2)
    print(s2.get_data())

    print(s1)
    print(s1.get_data())
