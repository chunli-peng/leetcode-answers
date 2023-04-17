class Solution:
    """
    Approach 1: Brute Force
    time: O(mn), space: O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if n < m:
            return -1

        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1


class Solution:
    """
    Approach 2: KMP, Knuth-Morris-Pratt algorithm
    time: O(m+n), space: O(m) for <lps>, where m=len(needle)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """Knuth-Morris-Pratt algorithm to check if 'needle' is in 'haystack'."""
        m, n = len(needle), len(haystack)
        if m > n:
            return -1

        haystack_i, needle_i = 0, 0
        lps = self._get_lps_array(needle)
        while haystack_i < n:
            if needle[needle_i] == haystack[haystack_i]:  # Matched increment both
                needle_i += 1
                haystack_i += 1
                if needle_i == m:  # All characters matched
                    return haystack_i - m
            else:
                if needle_i == 0:  # Zero matched
                    haystack_i += 1
                else:
                    needle_i = lps[needle_i-1]  # Shift left
        return -1

    def _get_lps_array(self, needle: List) -> List:
        """Get Longest Proper Prefix which is also Suffix (LPS) array.
        Example  : ACABACACD
        LPS Array: 001012320
        """
        m = len(needle)
        lps = [0] * m  # lps[0] will always be 0
        prev, curr = 0, 1
        while curr < m:
            if needle[curr] == needle[prev]:
                prev += 1  # Length of Longest Border Increased
                lps[curr] = prev
                curr += 1
            else:
                if prev == 0:  # Only empty border exist
                    lps[curr] = 0
                    curr += 1
                else:  # Try finding longest border for this curr with reduced prev
                    prev = lps[prev-1]
        return lps
