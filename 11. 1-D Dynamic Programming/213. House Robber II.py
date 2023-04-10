class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            n = len(nums)
            dp = [0] + [nums[0]] + [0] * (n-1)
            for i in range(2, n+1):
                # since array <dp> has dummy head, nums[i] should be nums[i-1]
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            n = len(nums)
            prev, curr = 0, nums[0]
            for i in range(1, n):
                prev, curr = curr, max(curr, prev+nums[i])
            return curr
        return max(helper(nums[1:]), helper(nums[:-1]))
