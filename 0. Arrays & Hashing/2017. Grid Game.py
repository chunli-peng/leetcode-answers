class Solution:
    """
    Approach 1: Prefix Sum
    time: O(n), space: O(n)
    """
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix = [0] * n  # second row
        suffix = [0] * n  # first row
        for i in range(n-1):
            prefix[i+1] = prefix[i] + grid[1][i]
        for i in range(n-1, 0, -1):
            suffix[i-1] = suffix[i] + grid[0][i]

        res = float('inf')
        for i in range(n):
            res = min(res, max(suffix[i], prefix[i]))
        return res


class Solution:
    """
    Approach 1.2: Prefix Sum (Rolling Array)
    time: O(n), space: O(1)
    """
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float("inf")
        prefix, suffix = 0, sum(grid[0])

        for r1, r2 in zip(grid[0], grid[1]):
            suffix -= r1
            res = min(res, max(prefix, suffix))
            prefix += r2
        return res
