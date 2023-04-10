class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            next = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, next
        return curr


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(n), space: O(n)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {0: 0, 1: 0}

        def dfs(n):
            if n in cache:
                return cache[n]
            cache[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return cache[n]
        return dfs(len(cost))


class Solution:
    """
    Approach 2.2: Recursive DFS + Memory Search (Built-in Func)
    time: O(n), space: O(n)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(n):
            if n == 0 or n == 1:
                return 0
            res = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return res
        return dfs(len(cost))
