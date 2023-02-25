class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(mn),
    space: O(mn) for hash table <pacific> <atlantic>, O(mn) for function stack,
        totally O(mn).
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, pre_h):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                heights[i][j] < pre_h or
                (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in direction:
                dfs(i+di, j+dj, visited, heights[i][j])

        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])

        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <pacific> <atlantic>, O(min(m,n)) for <queue>,
        totally, O(mn).
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        def bfs(i, j, visited):
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                for dx, dy in direction:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        heights[x+dx][y+dy] >= heights[x][y] and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for j in range(n):
            bfs(0, j, pacific)
            bfs(m-1, j, atlantic)

        for i in range(m):
            bfs(i, 0, pacific)
            bfs(i, n-1, atlantic)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <pacific> <atlantic>, O(min(m,n)) for <stack>,
        totally, O(mn).
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        def bfs(i, j, visited):
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in direction:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        heights[x+dx][y+dy] >= heights[x][y] and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for j in range(n):
            bfs(0, j, pacific)
            bfs(m-1, j, atlantic)

        for i in range(m):
            bfs(i, 0, pacific)
            bfs(i, n-1, atlantic)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res
