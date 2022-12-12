class Solution:
    """
    Approach 1: Sliding Window
    time: O(n), space: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        cur_val, max_val = 0, 0
        n = len(prices)
        for t in range(1, n):
            delta = prices[t] - prices[t-1]
            cur_val = max(delta, delta + cur_val)
            max_val = max(cur_val, max_val)
        return max_val
