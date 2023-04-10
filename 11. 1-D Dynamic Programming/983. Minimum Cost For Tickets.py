class Solution:
    """
    Approach 1: Dynamic Programming
    time: O((1+7+30)*n)=O(n), space: O(n)
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] + [float('inf')] * n

        for left in range(n):
            for delta, cost in zip([1, 7, 30], costs):
                right = left
                while right < n and days[right] < days[left]+delta:
                    right += 1
                dp[right] = min(dp[right], dp[left]+cost)
        return dp[n]


class Solution:
    """
    Approach 1.2: Dynamic Programming (alternative code)
    time: O((1+7+30)*n)=O(n), space: O(n)
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = {0: 0}

        for left in range(n):
            for delta, cost in zip([1, 7, 30], costs):
                right = left
                while right < n and days[right] < days[left]+delta:
                    right += 1
                dp[right] = min(dp.get(right, float('inf')), dp[left]+cost)
        return dp[n]


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O((1+7+30)*n)=O(n), space: O(n)
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = {}

        def dfs(left=0):
            if left == n:
                return 0
            if left in cache:
                return cache[left]

            cache[left] = float('inf')
            for delta, cost in zip([1, 7, 30], costs):
                right = left
                while right < n and days[right] < days[left]+delta:
                    right += 1
                cache[left] = min(cache[left], cost+dfs(right))
            return cache[left]
        return dfs()
