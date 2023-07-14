class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    Requirement: time: O(logn), space: O(1)
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution:
    """
    Approach 1.2: Binary Search
    time: O(logn), space: O(1)
    Requirement: time: O(logn), space: O(1)
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
