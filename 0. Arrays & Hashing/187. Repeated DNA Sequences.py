class Solution:
    """
    Approach 1: Hash Table
    time: O(L*n), space: O(L*n), where L = 10
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        res, seen = set(), set()
        for i in range(len(s)-L+1):
            sub = s[i:i+L]
            if sub in seen:
                res.add(sub)
            seen.add(sub)
        return list(res)


class Solution:
    """
    Approach 2: Hash Table + Sliding Window + Bit Manipulation
    details: use binary notation:
                A-00, C-01, G-10, T-11
    time: O(n), space: O(n)
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        n = len(s)
        if n <= L:
            return []
        res, seen = set(), set()
        window = 0

        # Initializing the sliding window
        for ch in s[:L-1]:
            window = (window << 2) | bin[ch]

        # Moving the window
        for i in range(n-L+1):
            window = ((window << 2) | bin[s[i+L-1]]) & ((1 << (2*L)) - 1)
            # details: 1. shift bits left
            #          2. add right character
            #          3. clear bigger 20 bits to 0
            if window in seen:
                res.add(s[i:i+L])
            seen.add(window)
        return list(res)
