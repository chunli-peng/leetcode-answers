class Solution:
    """
    Approach 1: Multi-source BFS
    time: O(n^2)
    space: O(n^2) for <dist>, O(n^2) for <queue>,
        totally, O(n^2).
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []

        for x in range(n):
            for y in range(n):
                if grid[x][y]:
                    queue.append((x, y))

        res = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = copy.deepcopy(grid)

        while queue:
            x, y = queue.pop(0)
            res = dist[x][y]
            for dx, dy in directions:
                if (
                    0 <= x+dx < n and
                    0 <= y+dy < n and
                    dist[x+dx][y+dy] == 0
                ):
                    queue.append([x+dx, y+dy])
                    dist[x+dx][y+dy] = dist[x][y] + 1

        return res - 1 if res > 1 else -1


class Solution:
    """
    Approach 2: Dynamic Programming
    time: O(n^2),
    space: O(n^2) for <dp>.
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = -1
        dp = copy.deepcopy(grid)

        for x in range(n):
            for y in range(n):
                dp[x][y] = 0 if grid[x][y] == 1 else float('inf')

        # from top left to bottom right
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    continue
                if x-1 >= 0:
                    dp[x][y] = min(dp[x-1][y] + 1, dp[x][y])
                if y-1 >= 0:
                    dp[x][y] = min(dp[x][y-1] + 1, dp[x][y])

        # reverse:
        for x in range(n-1, -1, -1):
            for y in range(n-1, -1, -1):
                if grid[x][y] == 1:
                    continue
                if x+1 < n:
                    dp[x][y] = min(dp[x+1][y] + 1, dp[x][y])
                if y+1 < n:
                    dp[x][y] = min(dp[x][y+1] + 1, dp[x][y])

                res = max(dp[x][y], res)

        return -1 if res == float('inf') else res
