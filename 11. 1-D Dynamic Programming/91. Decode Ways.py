class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2] != "0" and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev_prev, prev, curr = 0, 1, 0
        for i in range(1, n + 1):
            curr = 0
            if s[i-1] != '0':
                curr += prev
            if i != 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                curr += prev_prev
            prev_prev, prev = prev, curr
        return curr


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(n), space: O(n)
    """
    def __init__(self) -> None:
        self.cache = {}

    def numDecodings(self, s: str) -> int:
        def dfs(s=s):
            if s in self.cache:
                return self.cache[s]
            if s and int(s[0]) == 0:
                return 0
            if len(s) <= 1:
                return 1
            if int(s[:2]) <= 26:
                self.cache[s] = dfs(s[1:]) + dfs(s[2:])
                return self.cache[s]
            self.cache[s] = dfs(s[1:])
            return self.cache[s]
        return dfs()


class Solution:
    """
    Approach 2.2: Recursive DFS + Memory Search (Built-in Func)
    time: O(n), space: O(n)
    """
    @cache
    def numDecodings(self, s: str) -> int:
        if s and int(s[0]) == 0:
            return 0
        if len(s) <= 1:
            return 1
        if int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])
