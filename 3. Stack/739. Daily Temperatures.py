class Solution:
    """
    Approach 1: Monotonic Stack
    time: O(n), space: O(n)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # the indices of monotonically decreasing temperatures
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
