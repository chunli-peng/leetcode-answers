class Solution:
    """
    Approach 1: Sliding Window
    time: O(n), space: O(1)
    """
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cnt = sum(self._is_vowel(s[i]) for i in range(k))
        res = cnt
        for i in range(k, n):
            cnt += self._is_vowel(s[i]) - self._is_vowel(s[i-k])
            res = max(res, cnt)
        return res

    def _is_vowel(self, ch):
        return int(ch in "aeiou")


class Solution:
    """
    Approach 1.2: Sliding Window
    time: O(n), space: O(1)
    """
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = cnt = 0

        for right in range(len(s)):
            if s[right] in vowels:
                cnt += 1
            if right >= k:
                if s[right-k] in vowels:
                    cnt -= 1
            res = max(res, cnt)
        return res
