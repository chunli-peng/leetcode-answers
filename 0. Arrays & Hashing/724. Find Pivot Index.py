"""
Note: This question is the same as 1991
"""


class Solution:
    """
    Approach 1: Prefix Sum
    time: O(n), space: O(1)
    """
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        prefix = 0
        for i in range(len(nums)):
            suffix = total - nums[i] - prefix
            if prefix == suffix:
                return i
            prefix += nums[i]
        return -1
