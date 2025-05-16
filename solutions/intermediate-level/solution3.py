
# Implementation of LRU Cache using OrderedDict
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return None
        else:
            # Move the accessed item to the end of the OrderedDict
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move it to the end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the first (least recently used) item
            self.cache.popitem(last=False)


# Example usage
cache = LRUCache(2)
cache.put(1, 5)
cache.put(2, 2)
print(cache.get(1))  # returns 5
cache.put(3, 3)      # evicts key 2
print(cache.get(2))  # returns None (not found)
cache.put(4, 4)      # evicts key 1
print(cache.get(1))  # returns None (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4
