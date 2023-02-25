class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(mn),
    space: O(mn) for hash table <visited>, O(mn) for function stack,
        totally O(mn).
    """
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid1), len(grid1[0])
        res = 0
        visited = set()

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                grid2[i][j] == 0 or
                (i, j) in visited
            ):
                return True
            visited.add((i, j))
            flag = False if grid1[i][j] == 0 else True
            for di, dj in direction:
                flag = dfs(i+di, j+dj) and flag
            return flag

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and dfs(i, j):
                    res += 1
        return res


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <queue>,
        totally, O(mn).
    """
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid1), len(grid1[0])
        res = 0
        visited = set()

        def bfs(i, j):
            queue = [(i, j)]
            visited.add((i, j))
            flag = grid1[i][j] == 1
            while queue:
                x, y = queue.pop(0)
                flag = (grid1[x][y] == 1) and flag
                for dx, dy in direction:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid2[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            return flag

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and bfs(i, j):
                    res += 1
        return res


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <stack>,
        totally, O(mn).
    """
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid1), len(grid1[0])
        res = 0
        visited = set()

        def bfs(i, j):
            stack = [(i, j)]
            visited.add((i, j))
            flag = grid1[i][j] == 1
            while stack:
                x, y = stack.pop()
                flag = (grid1[x][y] == 1) and flag
                for dx, dy in direction:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        grid2[x+dx][y+dy] == 1 and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            return flag

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and bfs(i, j):
                    res += 1
        return res
