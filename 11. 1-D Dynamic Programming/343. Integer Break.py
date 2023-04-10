class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(n)
    """
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(n^2), space: O(n)
    """
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(num=n):
            if num in cache:
                return cache[num]
            cache[num] = 0 if num == n else num
            for i in range(num):
                cache[num] = max(cache[num], dfs(i)*dfs(num-i))
            return cache[num]
        return dfs()


class Solution:
    """
    Approach 3: Dynamic Programming + Math
    time: O(n), space: O(n)
    """
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3*dp[i-3])

        return dp[n]


class Solution:
    """
    Approach 4: Math
    time: O(1), space: O(1)
    """
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2
