class MyHashMap:
    """
    Approach 1: Brute Force (Big Array)
    time: O(1), space: O(C)
    """
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


class MyHashMap:
    """
    Approach 2: Chained Hashing (Unfixed-length Array)
    time: O(n/P), where P is prime number
    space: O(n+P)
    """
    def __init__(self):
        self.BASE = 1009
        self.buckets = [[] for _ in range(self.BASE)]

    def _hash(self, key: int) -> int:
        return key % self.BASE

    def put(self, key: int, value: int) -> None:
        hashkey = self._hash(key)
        for pair in self.buckets[hashkey]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self._hash(key)
        for pair in self.buckets[hashkey]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self._hash(key)
        for i, pair in enumerate(self.buckets[hashkey]):
            if pair[0] == key:
                self.buckets[hashkey].pop(i)
                return


class MyHashMap:
    """
    Approach 3: Chained Hashing (Fixed-length Array)
    time: O(1), space: O(C)
    """
    def __init__(self):
        self.map = [[-1] * 1000 for _ in range(1001)]

    def put(self, key, value):
        row, col = key // 1000, key % 1000
        self.map[row][col] = value

    def get(self, key):
        row, col = key // 1000, key % 1000
        return self.map[row][col]

    def remove(self, key):
        row, col = key // 1000, key % 1000
        self.map[row][col] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
