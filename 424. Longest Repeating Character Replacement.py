class Solution:
    """
    Approach 1: Sliding Window
    time: O(n)
    space: O(|Σ|), where |Σ| is the number of distinct characters in the string.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count, res, left, max_freq = {}, 0, 0, 0
        for right, ch in enumerate(s):
            count[ch] = 1 + count.get(ch, 0)
            max_freq = max(count[ch], max_freq)
            len_wind = right - left + 1
            if len_wind - max_freq > k:
                count[s[left]] -= 1
                left += 1
                len_wind -= 1
            res = max(res, len_wind)
        return res
