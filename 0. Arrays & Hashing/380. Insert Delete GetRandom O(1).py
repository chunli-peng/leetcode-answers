class RandomizedSet:
    """
    Approach 1: Variable-length Array + Hash Table
    time: O(1), space: O(n)
    """
    def __init__(self):
        self.nums = []
        self.indices = {}  # {num: index}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val]
        self.nums[index] = self.nums[-1]
        self.indices[self.nums[index]] = index
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
