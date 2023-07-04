class Solution:
    """
    Approach 1: Two Pointers
    time: O(m+n), space: O(1)
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        mergetd = ''

        while i < m and j < n:
            mergetd += word1[i]
            mergetd += word2[j]
            i += 1
            j += 1

        if i == m:
            mergetd += word2[j:]
        else:
            mergetd += word1[i:]

        return mergetd
