class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    Requirement: time: O(logn)
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                right = mid - 1
            elif mid < n-1 and nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                return mid
