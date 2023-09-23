class Solution:
    """
    Approach 1: Binary Search
    time: O(n), space: O(1)
    Follow-up Requirement: This problem is similar to 33.Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
    """
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:  # left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:  # right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
