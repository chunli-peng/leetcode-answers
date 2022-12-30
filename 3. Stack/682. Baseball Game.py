class Solution:
    """
    Approach 1: Stack
    time: O(n), space:(n)
    """
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == "+":
                stack.append(stack[-1]+stack[-2])
            elif ch == "D":
                stack.append(stack[-1]*2)
            elif ch == "C":
                stack.pop()
            else:
                stack.append(int(ch))
        return sum(stack)
