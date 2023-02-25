class Solution:
    """
    Approach 1: DFS + BFS + Hash Table
    time: O(n^2)
    space: O(n^2) for hash table <visited>, O(n) for function stack,
        O(n^2) for <queue>, totally, O(n^2).
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(i, j):
            """Find and Tag the island."""
            if (
                i < 0 or i >= n or
                j < 0 or j >= n or
                grid[i][j] == 0 or
                (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in directions:
                dfs(i+di, j+dj)

        def bfs():
            """Find and Return the shortest distance."""
            res = 0
            queue = list(visited)
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.pop(0)
                    for dx, dy in directions:
                        if (
                            0 <= x+dx < n and
                            0 <= y+dy < n and
                            (x+dx, y+dy) not in visited
                        ):
                            if grid[x+dx][y+dy] == 1:
                                return res
                            queue.append((x+dx, y+dy))
                            visited.add((x+dx, y+dy))
                res += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(n^2)
    space: O(n^2) for hash table <visited>, O(n) for <queue> in bfs_find_island
        O(n^2) for <queue> in bfs_dist, totally, O(n^2).
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs_find_island(i, j):
            """Find and Tag the island."""
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if (
                        0 <= x+dx < n and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        def bfs_dist():
            """Find and Return the shortest distance."""
            res = 0
            queue = list(visited)
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.pop(0)
                    for dx, dy in directions:
                        if (
                            0 <= x+dx < n and
                            0 <= y+dy < n and
                            (x+dx, y+dy) not in visited
                        ):
                            if grid[x+dx][y+dy] == 1:
                                return res
                            queue.append((x+dx, y+dy))
                            visited.add((x+dx, y+dy))
                res += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_find_island(i, j)
                    return bfs_dist()


class Solution:
    """
    Approach 3: Iterative DFS + BFS + Hash Table
    time: O(n^2)
    space: O(n^2) for hash table <visited>, O(n) for <stack>, O(n^2) for <queue>,
        totally, O(n^2).
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs_find_island(i, j):
            """Find and Tag the island."""
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    if (
                        0 <= x+dx < n and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        def bfs_dist():
            """Find and Return the shortest distance."""
            res = 0
            queue = list(visited)
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.pop(0)
                    for dx, dy in directions:
                        if (
                            0 <= x+dx < n and
                            0 <= y+dy < n and
                            (x+dx, y+dy) not in visited
                        ):
                            if grid[x+dx][y+dy] == 1:
                                return res
                            queue.append((x+dx, y+dy))
                            visited.add((x+dx, y+dy))
                res += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs_find_island(i, j)
                    return bfs_dist()
