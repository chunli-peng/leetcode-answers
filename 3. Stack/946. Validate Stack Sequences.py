class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for ch in pushed:
            stack.append(ch)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return not stack
