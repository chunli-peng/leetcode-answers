class Solution:
    """
    Approach 1: Sliding Window
    time: O(m) for initially counting, O(n-m) for moving window with O(Σ) checking,
        totally, O(m+(n-m)*Σ), where m=len(p), n=len(s)
    space: O(Σ)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        res = []
        window = [0] * 26
        p_count = [0] * 26
        for i in range(m):
            window[ord(s[i])-97] += 1
            p_count[ord(p[i])-97] += 1

        if window == p_count:
            res.append(0)
        for i in range(n-m):
            window[ord(s[i])-97] -= 1
            window[ord(s[i+m])-97] += 1
            if window == p_count:
                res.append(i+1)
        return res


class Solution:
    """
    Approach 2: Sliding Window
    time: O(m) for initially counting, O(Σ) for initializing <diff>,
        O(n-m) for moving window with O(1) checking,
        totally, O(m+n+Σ), where m=len(p), n=len(s)
    space: O(Σ)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        res = []
        counter = [0] * 26
        for i in range(m):
            counter[ord(s[i])-97] += 1
            counter[ord(p[i])-97] -= 1

        diff = [c != 0 for c in counter].count(True)
        if diff == 0:
            res.append(0)

        for i in range(n-m):
            # left:
            if counter[ord(s[i])-97] == 1:
                diff -= 1
            elif counter[ord(s[i])-97] == 0:
                diff += 1
            counter[ord(s[i])-97] -= 1
            # right:
            if counter[ord(s[i+m])-97] == -1:
                diff -= 1
            elif counter[ord(s[i+m])-97] == 0:
                diff += 1
            counter[ord(s[i+m])-97] += 1

            if diff == 0:
                res.append(i + 1)

        return res
