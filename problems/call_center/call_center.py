from typing import List
from collections import deque
from employee import Fresher, Lead, Manager
from request import IRequest, Status, Call
from levels import EmployeeLevel


class CallCenter:
    def __init__(self, manager: Manager):
        self.manager: List[manager] = [manager]
        self.freshers: List[Fresher] = []
        self.leads: List[Lead] = []
        self.request_queue: deque[IRequest] = deque()

    def add_fresher(self, fresher: Fresher) -> None:
        self.freshers.append(fresher)

    def add_lead(self, lead: Lead) -> None:
        self.lead.append(lead)

    def change_manager(self, manager: Manager) -> None:
        self.manager = manager

    def queue_request(self, request: IRequest):
        self.request_queue.append(request)

    def assign_request(self) -> None:
        if not self.request_queue:
            return

        request = self.request_queue.popleft()

        employee_pool = self.freshers
        if request.severity == EmployeeLevel.Lead:
            employee_pool = self.leads
        elif request.severity == EmployeeLevel.Manager:
            employee_pool = self.manager

        for e in employee_pool:
            if e.available:
                e.take_call(request)
                break

        # re-queue request if not taken by anyone
        if request.status == Status.Open:
            print("No one is available to take request. Request re-queued")
            self.queue_request(request)


if __name__ == "__main__":
    a = Manager("some name")
    center = CallCenter(a)

    call = Call(1, "customer1", EmployeeLevel.Lead)

    center.queue_request(call)
    center.add_fresher(Fresher("f1"))

    print(center.request_queue)

    center.assign_request()
