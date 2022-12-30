class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n+|Σ|), where Σ is character set for hash table
    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        Map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for ch in s:
            if ch in Map:
                if not stack or stack[-1] != Map[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
