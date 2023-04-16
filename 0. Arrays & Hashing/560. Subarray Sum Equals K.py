class Solution:
    """
    Approach 1: Prefix Sum + Hash Table
    time: O(n), space: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hashtable = {0: 1}
        pre_sum = 0
        for num in nums:
            pre_sum += num
            if pre_sum-k in hashtable:
                res += hashtable[pre_sum-k]
            hashtable[pre_sum] = hashtable.get(pre_sum, 0) + 1
        return res
