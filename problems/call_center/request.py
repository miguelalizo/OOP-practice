from __future__ import annotations
from abc import ABC
from enum import Enum
from levels import EmployeeLevel


class Status(Enum):
    """
    Status of a request
    """

    Open = 1
    InWork = 2
    Complete = 3


class IRequest(ABC):
    def __init__(
        self,
        id: int,
        customer: str,
        severity: EmployeeLevel,
    ):
        self.id = id
        self.customer = customer
        self.severity = severity
        self.status = Status.Open


class Call(IRequest):
    def __init__(self, id: int, customer: str, severity: EmployeeLevel):
        super().__init__(id, customer, severity)
