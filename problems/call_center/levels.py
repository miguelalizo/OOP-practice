from enum import Enum


class EmployeeLevel(Enum):
    """
    Level of an employee. Each level represents the level of request they can handle.
    """

    Fresher = 1
    Lead = 2
    Manager = 3
