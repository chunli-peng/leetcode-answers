class Solution:
    """
    Approach 1: Sliding Window
    time: O(|s|+|t|), space: O(|Σ|), where Σ is the character set of t
    """
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ''

        res, res_len = [None, None], float('infinity')
        need = n
        counter = collections.Counter(t)

        left = 0
        for right in range(m):
            ch = s[right]
            if ch in counter:
                if counter[ch] > 0:
                    need -= 1
                counter[ch] -= 1

            while need == 0:
                if right-left+1 < res_len:
                    res, res_len = [left, right], right-left+1

                ch = s[left]
                if ch in counter:
                    if counter[ch] >= 0:
                        need += 1
                    counter[ch] += 1
                left += 1

        return s[res[0]: res[1]+1] if res_len != float('infinity') else ''
