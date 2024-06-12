"""
Implement a dictionary

Assumptions:
    1. keys are integers
    2. can use chaining for collisions
    3. data will fit in memory (do not worry about alloocating extra space to the dict)
    4. Assume inputs are valid
"""

class Item:
    def __init__(self, key, value):
        self.key = key
        self.val = value


class MyDict:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.values = [[] for _ in range(self.capacity)] # List[List[Item]]
        self.size = 0

    def get(self, key):
        """
        Used for retrieving values from keys
        """
        index = self._hash(key)
        for item in self.values[index]:
            if item.key == key: return item.val
        raise Exception("Key Error")

    def insert(self, key, value):
        """
        Used for new key/value pairs and updating a value.
        Increments size
        """
        index = self._hash(key)
        for item in self.values[index]:
            if item.key == key:
                raise Exception("Key Value pair already exists")
        self.values[index].append(Item(key, value))
        self.size += 1

    def delete(self, key):
        """
        Used for deleting key-value pairs.
        Decrements size
        """
        table_index = self._hash(key)
        i = self._get_pos(table_index, key)

        if i == -1: raise Exception("Key Error. Cannot delete key-value pair that doesnt exist")

        self.values[table_index].pop(i)
        self.size -= 1

    def update(self, key, value):
        """
        Used for updating key-value pair.
        """
        table_index = self._hash(key)
        i = self._get_pos(table_index, key)

        if i == -1: raise Exception("Key Error. Cannot update key-value pair that doesnt exist")

        self.values[table_index][i].val = value

    def get_size(self) -> int:
        """
        Returns the current size of the dict
        """
        return self.size

    def _hash(self, key) -> int:
        """
        Modulo hashing function. Assumes key will always be an integer
        """
        return key % self.capacity

    def _get_pos(self, index, key):
        """
        Helper function
        Returns position of key-value pair in list for a particular hash_value (index)
        If not found, returns -1
        """
        i = len(self.values[index]) - 1
        while i > 0:
            if key == self.values[index][i].key:
                break
            i -= 1
        return i

"""
Unit tests
"""

def test_get():
    d = MyDict()
    d.insert(1, "hello1")
    d.insert(11, "hello11")
    d.insert(111, "hello111")
    assert("hello1" == d.get(1))

def test_insert():
    d = MyDict()
    d.insert(1, "hello1")
    assert(d.values[1][0].key == 1)
    assert(d.values[1][0].val == "hello1")
    assert(d.get_size() == 1)

def test_delete():
    d = MyDict()
    d.insert(1, "hello1")
    d.delete(1)
    assert(d.values[1] == [])
    assert(d.get_size() == 0)

def test_update():
    d = MyDict()
    d.insert(1, "hello1")
    d.update(1, "goodbye1")
    assert(d.values[1][0].val == "goodbye1")

def test_hash():
    assert(1 == MyDict()._hash(1))

def test_size():
    d = MyDict()
    assert(d.get_size() == 0)

def test_get_pos():
    d = MyDict(10)
    d.insert(1, "foo")
    d.insert(11, "bar")
    d.insert(101, "baz")

    assert(d._get_pos(1, 1) == 0)
    assert(d._get_pos(1, 11) == 1)
    assert(d._get_pos(1, 101) == 2)