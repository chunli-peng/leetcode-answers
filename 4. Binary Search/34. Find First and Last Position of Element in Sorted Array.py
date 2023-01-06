class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_boundary = self.binarysearch(nums, target)
        right_boundary = self.binarysearch(nums, target+1)
        if left_boundary == len(nums) or nums[left_boundary] != target:
            return [-1, -1]
        else:
            return [left_boundary, right_boundary-1]

    def binarysearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
