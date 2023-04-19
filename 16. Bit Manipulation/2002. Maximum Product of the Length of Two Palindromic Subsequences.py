class Solution:
    """
    Approach 1: Bit Manipulation + Bit Mask
    time: O(n*2^n) for filling <hashtable>,
        O(2^(n/2)*2^(n/2))=O(2^n) for calculate the result，
        totally, O(n*2^n)
    space: O(2^(n/2))
    """
    def maxProduct(self, s: str) -> int:
        n = len(s)
        hashtable = {}  # {mask: length}
        for mask in range(1, 1 << n):  # 1<<n = 2^n
            subseq = ''
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                hashtable[mask] = len(subseq)

        res = 0
        for i in hashtable:
            for j in hashtable:
                if i & j == 0:  # disjoint
                    res = max(res, hashtable[i]*hashtable[j])
        return res


class Solution:
    """
    Approach 2: Dynamic Programming + Bit Manipulation + Bit Mask
    time: O(n^3), space: O(2^n)
    unfinished
    """
    def maxProduct(self, s: str) -> int:
        n = len(s)
        dp = [0] * (1 << n)
        for i in range(n):
            dp[1 << i] = 1
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    for k in range(1 << (i-j-1)):
                        dp[(k << (j+1)) | (1 << j) | (1 << i)] = dp[k << (j+1)] + 2
                else:
                    for k in range(1 << (i - j - 1)):
                        dp[(k << (j+1)) | (1 << j) | (1 << i)] = max(dp[(k << (j+1)) | (1 << j)],
                                                                     dp[(k << (j+1)) | (1 << i)])
        return max(dp[i] * dp[i ^ ((1 << n) - 1)] for i in range(1 << n))
