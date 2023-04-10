class Solution:
    """
    Approach 1: Monotonic Stack
    time: O(n), space: O(n)
    """
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9+7
        res = 0
        stack = []  # [(start, num), ...]
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        nums.append(0)  # the ending zero could pop the all elements in the stack, avoiding iteration again
        for right, num in enumerate(nums):
            temp = right
            while stack and stack[-1][1] > num:
                left, min_val = stack.pop()
                res = max(res, min_val*(prefix[right]-prefix[left]))
                temp = left
            stack.append((temp, num))

        return res % MOD
