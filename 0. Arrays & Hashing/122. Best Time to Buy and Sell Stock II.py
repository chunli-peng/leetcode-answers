class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        for i in range(1, n):
            delta = prices[i]-prices[i-1]
            dp[i] = max(dp[i-1]+delta, dp[i-1])
        return dp[-1]


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev, curr = 0, 0
        for i in range(1, n):
            delta = prices[i]-prices[i-1]
            curr = max(prev+delta, prev)
            prev = curr
        return curr


class Solution:
    """
    Approach 2: Greedy
    time: O(n), space: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(1, n):
            delta = prices[i]-prices[i-1]
            if delta > 0:
                res += delta
        return res
