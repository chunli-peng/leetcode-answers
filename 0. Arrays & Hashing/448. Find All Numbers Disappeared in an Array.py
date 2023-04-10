class Solution:
    """
    Approach 1: Hashtable
    time: O(n), space: O(n)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashtable = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in hashtable]


class Solution:
    """
    Approach 2: In-place Modification
    time: O(n), space: O(1)
    Follow-up requirement: time: O(n), space: O(1)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            i = (num-1) % n
            nums[i] += n
        res = [i+1 for i, num in enumerate(nums) if num <= n]
        return res
