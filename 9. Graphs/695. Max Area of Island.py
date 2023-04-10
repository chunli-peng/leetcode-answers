class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(mn),
    space: O(mn) for hash table <visited>, O(mn) for function stack,
        totally O(mn).
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == 0 or
                (i, j) in visited
            ):
                return 0
            visited.add((i, j))
            return 1 + sum([dfs(i+di, j+dj) for (di, dj) in directions])

        for i in range(m):
            for j in range(n):
                res = max(dfs(i, j), res)
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS
    time: O(mn), space: O(mn) for function stack
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == 0
            ):
                return 0
            grid[i][j] = 0
            return 1 + sum([dfs(i+di, j+dj) for (di, dj) in directions])

        for i in range(m):
            for j in range(n):
                res = max(dfs(i, j), res)
        return res


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <queue>,
        totally, O(mn).
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(i, j, temp=0):
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                temp += 1
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            nonlocal res
            res = max(res, temp)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return res


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <stack>,
        totally, O(mn).
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(i, j, temp=0):
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                temp += 1
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            nonlocal res
            res = max(res, temp)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return res
