from __future__ import annotations
from abc import ABC, abstractmethod


# 1. define the command interface


class ICommand(ABC):
    """
    Abtract base class for Command objects.
    Conctrete commands must implement the process method
    """

    def __init__(self, receiver):
        """
        Initializes a command with a receiver.

        Parameters
        ----------
        receiver: The object that will perform the aciton when the
        command is invoked
        """
        self.receiver = receiver

    @abstractmethod
    def process():
        """
        Execute method all ICommands must implement
        """
        pass


# 2. Implement concrete Commands


class ConcreteCommand(ICommand):
    """
    Concrete command that performs an action through the receiver
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        """
        Execute the command by deledgating the actin to the receiver
        """
        self.receiver.perform_action()


# 3. Create a receiver


class Receiver:
    """Receiver class that performs an action"""

    def perform_action(self):
        """
        Perform an action
        """
        print("Action performed in receiver")


# 4. Invoker


class Invoker:
    """
    Invoker class that triggers the execution of a command
    """

    def __init__(self):
        self.cmd = None

    def command(self, cmd: ICommand):
        """
        Set the command to be executed
        """
        self.cmd = cmd

    def execute(self):
        """
        Execute the command by invoking its process method
        """
        self.cmd.process()


if __name__ == "__main__":
    # create receiver
    receiver = Receiver()

    # creatye a concrete command and set its receiver
    cmd = ConcreteCommand(receiver)

    # create an invoker
    invoker = Invoker()

    # set the command of the invoker
    invoker.command(cmd)

    # execute the command
    invoker.execute()
