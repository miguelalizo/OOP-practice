from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from request import IRequest, Status, Call
from levels import EmployeeLevel


class IEmployee(ABC):
    def __init__(
        self,
        level: EmployeeLevel,
        name: str,
    ):
        self.name = name
        self.available: bool = True
        self.level: EmployeeLevel = level
        self.request: IRequest = None

    def handle_request(self) -> Optional[IRequest]:
        """
        Method to handle a request. All employees are capable of
        handling requests depending on severity.

        Assumes employee is capable of handling request
        """
        if not self.request:
            print("No request to be handled")
            return None

        print(f"Request handled by {self.level}: {self.name}")
        self.request.status = Status.Complete
        req = self.request
        self.request = None
        return req

    def take_call(self, request: IRequest) -> None:
        """
        Assumes employee can always take the request.

        Changes the request state to in work
        """
        if not request:
            print("Request must be valid to be taken")
            return

        self.request = request
        self.request.status = Status.InWork
        print(f"Request taken by {self.level}: {self.name}")

    @abstractmethod
    def escalate(self) -> Optional[IRequest]:
        pass


class Fresher(IEmployee):
    def __init__(self, name: str):
        super().__init__(EmployeeLevel.Fresher, name)

    def escalate(self, request: IRequest) -> Optional[IRequest]:
        """
        Freshers can only escalate to Leads
        """
        if not self.request:
            return None

        request.level = EmployeeLevel.Lead
        request.status = Status.Open
        return request


class Lead(IEmployee):
    def __init__(self, name: str):
        super().__init__(EmployeeLevel.Lead, name)

    def escalate(self, request: IRequest) -> Optional[IRequest]:
        """
        Freshers can only escalate to Managers
        """
        request.level = EmployeeLevel.Manager
        request.status = Status.Open
        return request


class Manager(IEmployee):
    def __init__(self, name: str):
        super().__init__(EmployeeLevel.Manager, name)

    def escalate(self) -> Optional[IRequest]:
        raise Exception("Manager cannot escalate requests.")


if __name__ == "__main__":
    m = Manager("manager1")
    lead = Lead("lead1")
    fresh1 = Fresher("f1")

    print(m.level)
    print(lead.level)
    print(fresh1.level)
    request = Call(1, "customer1", EmployeeLevel.Fresher)
    fresh1.take_call(request)

    fresh1.handle_request()
