class Solution:
    """
    Approach 1: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(mn) for <queue>,
        totally, O(mn).
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res, fresh_counts = 0, 0
        visited = set()
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_counts += 1

        while fresh_counts and queue:
            q_len = len(queue)
            for _ in range(q_len):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        fresh_counts -= 1
                        visited.add((x+dx, y+dy))
            res += 1
        return res if not fresh_counts else -1


class Solution:
    """
    Approach 2: BFS
    time: O(mn), space: O(mn) for <queue>
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res, fresh_counts = 0, 0
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_counts += 1

        while fresh_counts and queue:
            q_len = len(queue)
            for _ in range(q_len):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1
                    ):
                        queue.append((x+dx, y+dy))
                        fresh_counts -= 1
                        grid[x+dx][y+dy] = 2
            res += 1
        return res if not fresh_counts else -1
