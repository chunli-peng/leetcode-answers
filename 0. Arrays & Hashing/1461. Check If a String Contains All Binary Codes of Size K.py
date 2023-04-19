class Solution:
    """
    Approach 1: Hash Table
    time: O(kn), space: O(k*2^k)
    """
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < (1 << k) + k - 1:  # 1<<k = 2^k
            return False
            # detail: Since each position can be the starting character
            # of a substring, and there are 2^k substrings, at least
            # 2^k different starting positions are needed. For the last
            # substring, it must have k-1 characters. Therefore, the
            # minimum length of the string should be (2^k) + k-1.
        hashtable = set([s[i:i+k] for i in range(n-k+1)])
        return len(hashtable) == 1 << k


class Solution:
    """
    Approach 2: Sliding Window + Hash Table
    time: O(k*n), space: O(k*2^k)
    """
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < (1 << k) + k - 1:  # 1<<k = 2^k
            return False
            # detail: Since each position can be the starting character
            # of a substring, and there are 2^k substrings, at least
            # 2^k different starting positions are needed. For the last
            # substring, it must have k-1 characters. Therefore, the
            # minimum length of the string should be (2^k) + k-1.

        # Initializing the sliding window
        window = int(s[:k], base=2)
        hashtable = set([window])

        # Moving the window
        for i in range(1, n-k+1):
            window = (window - ((ord(s[i-1])-48) << (k-1))) * 2 + (ord(s[i+k-1])-48)
            # details: 1. delete left character
            #          2. shift bits left
            #          3. add right character
            # =================================================================
            # Another Approach:
            # window = ((window << 1) | int(s[i+k-1], base=2)) & ((1 << k) - 1)
            # details: 1. shift bits left
            #          2. add right character
            #          3. clear bigger k bits to 0
            # =================================================================
            hashtable.add(window)

        return len(hashtable) == (1 << k)
