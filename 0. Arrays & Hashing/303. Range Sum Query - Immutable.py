class NumArray:
    """
    Approach 1: Prefix Sum
    time: O(n) for __init__(), O(1) for sumRange()
    space: O(n)
    """
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
