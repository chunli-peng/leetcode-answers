class Solution:
    """
    Approach 1: Hash Table (from sides to center)
    time: O(n|Σ|), where Σ is the character set
    space: O(|Σ|)
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            left = s.index(c)
            right = s.rindex(c)
            res += len(set(s[left+1: right]))
        return res


class Solution:
    """
    Approach 2: Hash Table (from center to sides)
    time: O(n|Σ|), where Σ is the character set
    space: O(|Σ|)
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        res, left = set(), set()
        right = collections.Counter(s)

        for ch in s:
            right[ch] -= 1
            if right[ch] == 0:
                right.pop(ch)

            for ch_new in left:
                if ch_new in right:
                    res.add(ch_new+ch+ch_new)
            left.add(ch)
        return len(res)


class Solution:
    """
    Approach 3: Prefix Sum + Bit Manipulation + Bit Mask
    detail: Use 32-bit integers to represent the categories in string.
    time: O(n+|Σ|), where Σ is the character set
    space: O(|Σ|)
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        res = 0

        prefix, suffix = [0] * n, [0] * n
        for i in range(n):
            prefix[i] = (prefix[i-1] if i else 0) | (1 << (ord(s[i]) - ord('a')))
        for i in range(n-1, -1, -1):
            suffix[i] = (suffix[i+1] if i != n-1 else 0) | (1 << (ord(s[i]) - ord('a')))

        res_list = [0] * 26
        for i in range(1, n-1):
            res_list[ord(s[i])-ord('a')] |= prefix[i-1] & suffix[i+1]

        for item in res_list:
            res += bin(item).count("1")
        return res
