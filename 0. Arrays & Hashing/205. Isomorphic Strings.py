class Solution:
    """
    Approach 1: Two Hash Tables
    time: O(n), space: O(|Σ|), where Σ is the character set
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s_to_t = {}  # {s[i]: t[i]}
        t_to_s = {}  # {t[i]: s[i]}
        for i in range(n):
            if (s[i] in s_to_t and s_to_t[s[i]] != t[i]) or \
             (t[i] in t_to_s and t_to_s[t[i]] != s[i]):
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        return True


class Solution:
    """
    Approach 2: Index
    time: O(n), space: O(1)
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                # index() will return the fist index of input
                return False
        return True
