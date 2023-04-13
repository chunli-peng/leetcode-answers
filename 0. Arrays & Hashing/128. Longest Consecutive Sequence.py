class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n)
    Requirement: time: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        hashtable = set(nums)
        res = 0
        for num in hashtable:
            if num-1 not in hashtable:
                cur_len = 1
                while num+cur_len in hashtable:
                    cur_len += 1
                res = max(res, cur_len)
        return res
    