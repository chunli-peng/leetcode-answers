class Solution:
    """
    Approach 1: Monotonic Stack
    time: O(n), space: O(n)
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        stack = stack[:len(stack)-k]  # considering k!=0
        res = ''.join(stack)
        return str(int(res)) if res else '0'  # removing leading zeros
