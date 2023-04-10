class Solution:
    """
    Approach 1: Two Pointers
    time: O(m+n), space: O(1)
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


class Solution:
    """
    Approach 2: Dynamic Programming
    time: O(n*|Σ|) for initialization of DP table, O(m) for each check,
        totally, O(n*|Σ|+m), O(n*|Σ|+k*m) for k times check,
        O(n*|Σ|+k*m) << O(k*m+k*n) for Approach 1: Two Pointers
    space: O(n*|Σ|) for <dp>
    Follow-up requirement: Suppose there are lots of incoming <s>, where k>10^9
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        size = 26
        dp = [[0] * size for _ in range(n)]
        dp.append([n]*size)

        # Initialization DP table
        for i in range(n-1, -1, -1):
            for j in range(size):
                dp[i][j] = i if ord(t[i]) == ord('a')+j else dp[i+1][j]

        # check the string <s>
        find_i = 0
        for i in range(m):
            if dp[find_i][ord(s[i])-ord('a')] == n:
                return False
            find_i = dp[find_i][ord(s[i])-ord('a')] + 1
        return True
