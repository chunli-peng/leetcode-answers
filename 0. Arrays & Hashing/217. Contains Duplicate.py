class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()
        for num in nums:
            if num in hashtable:
                return True
            hashtable.add(num)
        return False
