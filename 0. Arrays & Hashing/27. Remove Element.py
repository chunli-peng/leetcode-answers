class Solution:
    """
    Approach 1: Two Pointers (two scans)
    time: O(n), space: O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


class Solution:
    """
    Approach 1.2: Two Pointers (one scan)
    time: O(n), space: O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
