"""
Code Example from Problem 200:
"""

class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(mn),
    space: O(mn) for hash table <visited>, O(mn) for function stack,
        totally O(mn).
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == '0' or
                (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in direction:
                dfs(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS
    time: O(mn), space: O(mn) for function stack, totally O(mn).
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == '0'
            ):
                return
            grid[i][j] = '0'
            for di, dj in direction:
                dfs(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <queue>,
        totally, O(mn).
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(i, j):
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == '1' and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    bfs(i, j)
        return res


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <stack>,
        totally, O(mn).
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(i, j):
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == '1' and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    bfs(i, j)
        return res


class Solution:
    """
    Approach 4: Union Find by Rank
    time: O(mn*α(mn)), where α is This inverse Ackermann function, \
        and α<5 for practical input.
    space: O(mn) for variable <parent>, <rank> in UnionFind.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        uf = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for di, dj in directions:
                        if (
                            0 <= i+di < m and
                            0 <= j+dj < n and
                            grid[i+di][j+dj] == '1'
                        ):
                            uf.union(i*n+j, (i+di)*n+(j+dj))
        return uf.get_counts()


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [None] * m * n
        self.rank = [0] * m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n+j] = i*n+j
                    self.count += 1

    def _find(self, x):
        """Find and Return the parent of the point <x>"""
        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Unite the point <x> and <y>"""
        root_x = self._find(x)
        root_y = self._find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            elif self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.parent[root_y] = root_x
            self.count -= 1

    def get_counts(self):
        """Return the result"""
        return self.count
