"""
Remote control system

By separating the abstraction of remote controls from
the implementation of devices, we achieved a modular and
extensible design.

You can easily add new devices and remote control types
without altering existing code, making your system more
maintainable and adaptable.

The Bridge Pattern is a valuable tool for creating elegant
and scalable solutions in software design.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


# abstraction
class RemoteControl:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, device: IDevice):
        self._device = device

    def volume_up(self):
        self._device.volume_up()

    def volume_down(self):
        self._device.volume_down()

    def toggle_power(self):
        self._device.toggle_power()


# implementation
class IDevice(ABC):
    """
    Device interface
    """

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def toggle_power(self):
        pass


# concrete implementations


class TV(IDevice):
    def volume_up(self):
        print("TV: raise volume")

    def volume_down(self):
        print("TV: lower volume")

    def toggle_power(self):
        print("TV: toggle power")


class SoundSystem(IDevice):
    def volume_up(self):
        print("SoundSystem: raise volume")

    def volume_down(self):
        print("SoundSystem: lower volume")

    def toggle_power(self):
        print("SoundSystem: toggle power")


# client code
if __name__ == "__main__":
    tv = TV()
    tv_remote = RemoteControl(tv)

    sound_system = SoundSystem()
    ss_remote = RemoteControl(sound_system)

    # client can use the RemoteControl (abstraction) in the same way
    # independently of what device (implementation) is being controled
    tv_remote.toggle_power()
    ss_remote.toggle_power()

    tv_remote.volume_down()
    ss_remote.volume_down()

    tv_remote.volume_up()
    ss_remote.volume_up()
