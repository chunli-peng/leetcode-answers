class Solution:
    """
    Approach 1: Sliding Window + Double string
    time: O(n), space: O(n)
    details: 1. the Type-1 operation is a sliding window actually.
            2. since the target strings are alternating, the required
            operations ( min(diff_0,diff_1) ) in the sliding window keep same.
    """
    def minFlips(self, s: str) -> int:
        n = len(s)
        res = n
        s += s  # double the string

        # create alternating strings started with "0" and "1":
        alt_start_0, alt_start_1 = "", ""
        for i in range(2*n):
            alt_start_0 += "0" if i % 2 else "1"
            alt_start_1 += "1" if i % 2 else "0"

        diff_0, diff_1 = 0, 0
        left = 0
        for right in range(2*n):
            # considering the right point of the window:
            if s[right] != alt_start_0[right]:
                diff_0 += 1
            if s[right] != alt_start_1[right]:
                diff_1 += 1
            len_wind = right-left+1  # the length of the window
            # considering the left point of the window:
            if len_wind == n+1:
                if s[left] != alt_start_0[left]:
                    diff_0 -= 1
                if s[left] != alt_start_1[left]:
                    diff_1 -= 1
                left += 1
                len_wind -= 1
            if len_wind == n:
                res = min(res, diff_0, diff_1)
        return res


class Solution:
    """
    Approach 1.2: Sliding Window + Imaginary Double string
    time: O(n), space: O(1)
    """
    def minFlips(self, s: str) -> int:
        target = '01'
        n, diff = len(s), 0
        for i in range(n):
            if s[i] != target[i % 2]:
                diff += 1
        res = min(diff, n - diff)

        # situation: even length
        # since s[i] = s[i + n], each window is same.
        if n % 2 == 0:
            return res

        # situation: odd length
        for i in range(n):
            if s[i] == target[i % 2]:
                diff += 1
            else:
                diff -= 1
            res = min(res, diff, n - diff)
        return res
