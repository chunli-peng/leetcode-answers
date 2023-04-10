class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [nums[0]] + [None]*(n-1)
        dp_min = [nums[0]] + [None]*(n-1)
        res = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            res = max(res, dp_max[i])
        return res


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def maxProduct(self, nums: List[int]) -> int:
        dp_max, dp_min, res = 1, 1, nums[0]
        for num in nums:
            dp_max, dp_min = max(dp_max*num, dp_min*num, num), \
                min(dp_max*num, dp_min*num, num)
            res = max(res, dp_max)
        return res
