from abc import ABC, abstractmethod


class OldSystem:
    """Legacy system that needs to be integrated into client_code"""

    def legacy_operation(self):
        return "Legacy operation"


class ISystem(ABC):
    """System interface"""

    @abstractmethod
    def new_operation(self):
        pass


class OldSystemAdapter(ISystem):
    """
    Adapter class that wraps the OldSystem object and
    provides a new method, new_operation()
    """

    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self):
        return f"OldSystem: Adapted {self.old_system.legacy_operation()}"


class NewSystem(ISystem):
    def new_operation(self):
        return "NewSystem: New operation"


# client code
def client_code(system):
    """Client code that needs to make use of legacy_system"""
    result = system.new_operation()
    print(result)


if __name__ == "__main__":
    new_system = NewSystem()
    old_system = OldSystem()
    adapted_old_system = OldSystemAdapter(old_system)

    # client code can safely call new_operation just
    # like it can the new system
    client_code(new_system)
    client_code(adapted_old_system)
