class Solution:
    """
    Approach 1: Two Pointers
    time: O(n), space: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        while curr < len(nums):
            count = 1
            while curr+1 < len(nums) and nums[curr] == nums[curr+1]:
                curr += 1
                count += 1
            for _ in range(min(2, count)):
                nums[prev] = nums[curr]
                prev += 1
            curr += 1
        return prev


class Solution:
    """
    Approach 1.2: Two Pointers (alternative code)
    time: O(n), space: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        slow = fast = 2
        while fast < len(nums):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
