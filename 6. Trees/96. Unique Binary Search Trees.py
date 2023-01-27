class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(n)
    """
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]


class Solution:
    """
    Approach 2: Catalan Number (Math)
    time: O(n), space: O(1)
    """
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C *= 2*(2*i+1)/(i+2)
        return int(C)


class Solution:
    """
    Approach 2.2: Catalan Number (Math) (alternative code)
    time: O(n), space: O(1)
    """
    def numTrees(self, n: int) -> int:
        import math
        return int(math.factorial(2*n) / math.factorial(n+1) / math.factorial(n))