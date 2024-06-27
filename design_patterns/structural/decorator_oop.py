from __future__ import annotations
from abc import ABC, abstractmethod
from time import time


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        pass


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bound: int) -> int:
        """inefficiently count primes"""
        count = 0
        for i in range(upper_bound):
            count += 1 if is_prime(i) else 0
        return count


class AbstractDecorator(AbstractComponent):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


class WithLogging(AbstractDecorator):

    def execute(self, upper_bound: int) -> int:
        print(f"WithLogging: start execution of {self._decorated.__class__}")
        res = self._decorated.execute(upper_bound)
        print("WithLogging: excetucion success")
        return res


class WithBenchmark(AbstractDecorator):

    def execute(self, upper_bound: int) -> int:
        start = time()
        print(f"WithBenchmark: start execution of {self._decorated.__class__}")
        res = self._decorated.execute(upper_bound)
        end = time()
        print(f"WithBenchmark: excetucion end: Time elapsed={end - start}")
        return res


def is_prime(n: int) -> bool:
    """Returns true if n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if i != n and n % i == 0:
            return False
    return True


if __name__ == "__main__":
    component = ConcreteComponent()
    with_logging = WithLogging(component)
    with_benchmark = WithBenchmark(with_logging)
    print(with_benchmark.execute(1000))
