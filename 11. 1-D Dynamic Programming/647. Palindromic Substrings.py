class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(n^2)
    """
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right-left <= 1 or dp[left+1][right-1]):
                    dp[left][right] = True
                    res += 1
        return res

class Solution:
    """
    Approach 2: Center Extension Method
    time: O(n^2), space: O(1)
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        for i in range(n):
            self._expand_center(s, i, i)
            self._expand_center(s, i, i+1)
        return self.res

    def _expand_center(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
            self.res += 1


class Solution:
    """
    Approach 3: Manacher Algorithm
    time: O(n), space: O(n)
    """
    def countSubstrings(self, s: str) -> int:
        res = 0
        s = '#' + '#'.join(list(s)) + '#'  # translate to odd string
        arm_len_list = []
        right = -1  # right end of the string
        j = -1  # center of palindrome string
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i  # symmetry point of <i>
                min_arm = min(arm_len_list[i_sym], right-i)
                cur_arm = self._expand_center(s, i-min_arm, i+min_arm)
            else:
                cur_arm = self._expand_center(s, i, i)
            arm_len_list.append(cur_arm)
            if i + cur_arm > right:
                j, right = i, i + cur_arm  # update
            res += (cur_arm + 1) // 2  # skip the '#'
        return res

    def _expand_center(self, s, left, right):
        """Expand the string and return the arm length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2
