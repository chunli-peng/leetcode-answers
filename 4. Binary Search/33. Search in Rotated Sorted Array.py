class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:  # left sorted portion
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right sorted portion
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
