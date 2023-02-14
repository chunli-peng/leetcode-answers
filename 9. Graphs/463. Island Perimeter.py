class Solution:
    """
    Approach 1: Recursive DFS
    time: O(mn), worst situation is scanning all cells.
    space: O(mn) for hash table <visited>, O(mn) for function stack.
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        res = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or not grid[i][j]:
                nonlocal res
                res += 1
                return
            if (i, j) not in visited:
                visited.add((i, j))
                for di, dj in directions:
                    dfs(i+di, j+dj)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    dfs(i, j)
        return res


class Solution:
    """
    Approach 2: Iteration
    time: O(4mn)=O(mn), space: O(1)
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    for di, dj in directions:
                        new_i, new_j = i+di, j+dj
                        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols \
                                or not grid[new_i][new_j]:
                            res += 1
        return res


class Solution:
    """
    Approach 2.2: Iteration (alternative code)
    time: O(2mn)=O(mn), space: O(1)
    detail: each land contribute 4, and every border contribute -2.
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    res += 4
                    if i < rows - 1 and grid[i+1][j]:
                        res -= 2
                    if j < cols - 1 and grid[i][j+1]:
                        res -= 2
        return res
