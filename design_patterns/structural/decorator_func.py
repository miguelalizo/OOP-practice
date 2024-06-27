from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, Any
from time import time


def benchmark(func: Callable[..., Any]) -> Callable[..., any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"WithBenchmark: excetucion end: Time elapsed={end - start}")
        return res

    return wrapper


def logger(func: Callable[..., Any]) -> Callable[..., any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Logger: start execution of {func.__name__}")
        res = func(*args, **kwargs)
        print("Logger: excetucion end")
        return res

    return wrapper


@logger
@benchmark
def count_primes(upper_bound: int) -> int:
    """inefficiently count primes"""
    count = 0
    for i in range(upper_bound):
        count += 1 if is_prime(i) else 0
    return count


def is_prime(n: int) -> bool:
    """Returns true if n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if i != n and n % i == 0:
            return False
    return True


if __name__ == "__main__":
    count_primes(1000)
