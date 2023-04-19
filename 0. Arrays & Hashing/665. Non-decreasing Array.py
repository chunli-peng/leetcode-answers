class Solution:
    """
    Approach 1: One Pass
    time: O(n), space: O(1)
    """
    def checkPossibility(self, nums: List[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if count > 0:
                    return False
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                count += 1
        return True