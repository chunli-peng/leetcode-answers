class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}  # pair: {val: index}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i
