class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # pair: [ch, count]
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            if stack[-1][1] == k:
                stack.pop()
        res = ''
        for ch, count in stack:
            res += ch * count
        return res
