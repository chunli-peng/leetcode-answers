class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
