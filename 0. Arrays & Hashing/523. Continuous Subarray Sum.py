class Solution:
    """
    Approach 1: Prefix Sum + Hash Table
    time: O(n), space: O(min(n,k))
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}  # {prefix % k: index}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            if prefix % k in hashmap:
                if i - hashmap[prefix % k] > 1:
                    return True
                else:  # Skip updating hashmap
                    continue  # Only record the first index of reminders
            hashmap[prefix % k] = i
        return False
