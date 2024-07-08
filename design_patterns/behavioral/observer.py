from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Set


# 1. Create subscriber interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        pass


# 2. Create concrete subscribers
class WeatherStationDisplay(Subscriber):
    def update(self, weather):
        temperature = weather.temp
        print(f"WeatherStation: Temperature is {temperature} degrees Celsius")


class PhoneDisplay(Subscriber):
    def update(self, weather):
        temperature = weather.temp
        print(f"PhoneDisplay: Temperature is {temperature} degrees Celsius")


# 3. Create publisher


class Publisher:
    def __init__(self, weather: Weather):
        self.subscribers: Set[Subscriber] = set()
        self.weather = weather

    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.weather)


class Weather:
    def __init__(self, temp: int):
        self.temp = temp

    def update(self, newtemp):
        self.temp = newtemp


if __name__ == "__main__":
    # observable weather
    w = Weather(10)
    # publisher
    pub = Publisher(w)

    # subscribers / observers
    phoneWidget = PhoneDisplay()
    station = WeatherStationDisplay()

    # add subscribers
    pub.add_subscriber(phoneWidget)
    pub.add_subscriber(station)

    # update / notify subscribers
    pub.notify_subscribers()

    # weather changes
    w.update(15)

    # update / notify subscribers
    pub.notify_subscribers()
