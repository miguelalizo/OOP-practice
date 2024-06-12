class Item:
    def __init__(self, key, value, left=None, right=None):
        self.key, self.val = key, value
        self.left = self.right = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {} # {key: Item}
        self.head, self.tail = Item(0, 0), Item(0, 0)
        self.head.right, self.tail.left = self.tail, self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.insert(self.delete(self.cache[key])).val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            item = Item(key, value)
            self.cache[key] = item
            if len(self.cache) > self.size:
                self.cache.pop(self.delete(self.head.right).key)
        else:
            item = self.delete(self.cache[key])
            item.val = value
        
        self.insert(item)
        
    def delete(self, item):
        prv, nxt = item.left, item.right
        prv.right, nxt.left = nxt, prv
        return item
    
    def insert(self, item):
        prv = self.tail.left
        item.right, self.tail.left = self.tail, item
        prv.right, item.left = item, prv
        return item

"""
Unit tests
"""

def test_put():
    cache = LRUCache(capacity=3)
    cache.put(1, "foo")
    assert(cache.cache[1].val == "foo")

    cache.put(2, "bar")
    assert(cache.cache[1].right == cache.cache[2])
    assert(cache.cache[2].left == cache.cache[1])

    cache.put(1, "baz")
    assert(cache.cache[1].val == "baz")
    assert(cache.cache[2].right == cache.cache[1])
    assert(cache.cache[1].left == cache.cache[2])

    cache.put(3, "lol")
    cache.put(4, "haha")
    assert(2 not in cache.cache)

def test_get():
    cache = LRUCache(capacity=3)
    cache.put(1, "foo")
    cache.put(2, "bar")
    cache.put(3, "lol")

    assert(cache.head.right == cache.cache[1])
    assert(cache.tail.left == cache.cache[3])

    assert(cache.get(1) == "foo")

    assert(cache.head.right == cache.cache[2])
    assert(cache.tail.left == cache.cache[1])

