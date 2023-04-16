class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)
        return (len(stack)//2 + 1) // 2


class Solution:
    """
    Approach 2: Greedy
    time: O(n), space: O(1)
    """
    def minSwaps(self, s: str) -> int:
        stack, res = 0, 0

        for ch in s:
            if ch == "[":
                stack -= 1
            else:
                stack += 1
            res = max(res, stack)

        return (res + 1) // 2  # Or math.ceil(res / 2)
