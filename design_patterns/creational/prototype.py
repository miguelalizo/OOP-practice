from copy import copy, deepcopy
from typing import List


class SomeComponent:
    def __init__(self, some_field: str, some_list_field: List):
        self.some_field = some_field
        self.some_list_field = some_list_field

    def __copy__(self):
        """
        Provides shallow copy capabilities for this class using the copy.copy function.
        This method will be called when someone calls copy.copy with this object.
        """

        return self.__class__(
            some_field=self.some_field, some_list_field=self.some_list_field
        )

    def __deepcopy__(self, memo=None):
        """
        Provides deep copy capabilities for this class using the copy.deepcopy function.
        This method will be called when someone calls copy.deepcopy with this object.
        """
        some_field = deepcopy(self.some_field)
        some_list_field = deepcopy(self.some_list_field)
        return self.__class__(some_field, some_list_field)


if __name__ == "__main__":
    componentA = SomeComponent("value1", [1, 2, 3])
    copyA = copy(componentA)
    deepcopyA = deepcopy(componentA)

    print(componentA)
    print(copyA)
    print(deepcopyA)

    print(id(componentA.some_list_field))
    print(id(copyA.some_list_field))
    print(id(deepcopyA.some_list_field))

    componentA.some_list_field.append(4)

    print(componentA.some_list_field)
    print(copyA.some_list_field)
    print(deepcopyA.some_list_field)

    assert copyA.some_list_field is componentA.some_list_field
    assert deepcopyA.some_list_field is not componentA.some_list_field
