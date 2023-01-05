class Solution:
    """
    Approach 1: Two Pointers
    time: O(n), space: O(1)
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n-1

        while left <= right:
            num_left, num_right = abs(nums[left]), abs(nums[right])
            if num_left > num_right:
                res[right-left] = num_left**2
                left += 1
            else:
                res[right-left] = num_right**2
                right -= 1
        return res
