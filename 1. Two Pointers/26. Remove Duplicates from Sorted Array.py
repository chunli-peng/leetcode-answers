class Solution:
    """
    Approach 1: Two Pointers
    time: O(n), space: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, curr, k = 0, 0, 1
        while curr < len(nums):
            if nums[prev] == nums[curr]:
                curr += 1
            else:
                nums[k] = nums[curr]
                prev = curr
                k += 1
        return k


class Solution:
    """
    Approach 1.2: Two Pointers (alternative code)
    time: O(n), space: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 1
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
