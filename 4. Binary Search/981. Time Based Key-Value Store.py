class TimeMap:
    """
    Approach 1: Binary Search + Hashtable
    time: O(1) for set(), O(logn) for get(),
    space: O(n)
    """
    def __init__(self):
        self.Hashtable = {}  # {key:[[val, timestamp], ...]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Hashtable:
            self.Hashtable[key] = []
        self.Hashtable[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.Hashtable.get(key, [])
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left+right)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid+1
            else:
                right = mid-1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)