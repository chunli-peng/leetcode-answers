class MyHashSet:
    """
    Approach 1: Brute Force (Big Array)
    time: O(1), space: O(C)
    """
    def __init__(self):
        self.map = [False] * 1000001

    def add(self, key: int) -> None:
        self.map[key] = True

    def remove(self, key: int) -> None:
        self.map[key] = False

    def contains(self, key: int) -> bool:
        return self.map[key]


class MyHashSet:
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

    def add(self, key: int) -> None:
        hashkey = self._hash(key)
        for item in self.buckets[hashkey]:
            if item == key:
                return
        self.buckets[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self._hash(key)
        for i, item in enumerate(self.buckets[hashkey]):
            if item == key:
                self.buckets[hashkey].pop(i)
                return

    def contains(self, key: int) -> bool:
        hashkey = self._hash(key)
        for item in self.buckets[hashkey]:
            if item == key:
                return True
        return False


class MyHashSet:
    """
    Approach 3: Chained Hashing (Fixed-length Array)
    time: O(1), space: O(C)
    """
    def __init__(self):
        self.map = [[False] * 1000 for _ in range(1001)]

    def add(self, key: int) -> None:
        row, col = key // 1000, key % 1000
        self.map[row][col] = True

    def remove(self, key: int) -> None:
        row, col = key // 1000, key % 1000
        self.map[row][col] = False

    def contains(self, key: int) -> bool:
        row, col = key // 1000, key % 1000
        return self.map[row][col]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
