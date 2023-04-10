class Solution:
    """
    Approach 1: 2-D Dynamic Programming
    time: O(n^2), space: O(n^2)
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * i for i in range(1, n+1)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[n-1])


class Solution:
    """
    Approach 1.2: 1-D Dynamic Programming (Rolling Array: O(2n))
    time: O(n^2), space: O(n)
    Follow-up requirement: space: O(n)
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev, curr = [0]*n, [0]*n
        prev[0] = triangle[0][0]

        for i in range(1, n):
            curr[0] = prev[0] + triangle[i][0]
            for j in range(1, i):
                curr[j] = min(prev[j-1], prev[j]) + triangle[i][j]
            curr[i] = prev[i-1] + triangle[i][i]
            prev = curr[:]
        return min(prev)


class Solution:
    """
    Approach 1.3: 1-D Dynamic Programming (Rolling Array: O(n))
    time: O(n^2), space: O(n)
    Follow-up requirement: space: O(n)
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [triangle[0][0]] + [0]*(n-1)

        for i in range(1, n):
            # reverse update: use the last state of dp[j-1]
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)


class Solution:
    """
    Approach 1.4: 1-D Dynamic Programming (Rolling Array: O(n)) (alternative code)
    time: O(n^2), space: O(n)
    Follow-up requirement: space: O(n)
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        # reverse iteration:
        for row in range(n-2, -1, -1):
            for col in range(0, row+1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
        return dp[0]
