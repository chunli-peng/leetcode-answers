class Solution:
    """
    Approach 1: Count
    time: O(n), space: O(1)
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(ch for ch in text if ch in "balon")
        counts['l'] //= 2
        counts['o'] //= 2
        return min(counts.values()) if len(counts) == 5 else 0
