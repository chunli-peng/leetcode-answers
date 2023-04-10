class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(mn),
    space: O(mn) for hash table <visited>, O(mn) for function stack,
        totally O(mn).
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                board[i][j] != 'O' or
                (i, j) in visited
            ):
                return
            board[i][j] = '#'
            visited.add((i, j))
            for di, dj in directions:
                dfs(i+di, j+dj)

        for i in range(m):
            if board[i][0] == 'O' and (i, 0) not in visited:
                dfs(i, 0)
            if board[i][n-1] == 'O' and (i, n-1) not in visited:
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and (0, j) not in visited:
                dfs(0, j)
            if board[m-1][j] == 'O' and (m-1, j) not in visited:
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <queue>,
        totally, O(mn).
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])
        visited = set()

        def bfs(i, j):
            queue = [(i, j)]
            visited.add((i, j))
            while queue:
                x, y = queue.pop(0)
                board[x][y] = '#'
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        board[x+dx][y+dy] == 'O' and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for i in range(m):
            if board[i][0] == 'O' and (i, 0) not in visited:
                bfs(i, 0)
            if board[i][n-1] == 'O' and (i, n-1) not in visited:
                bfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and (0, j) not in visited:
                bfs(0, j)
            if board[m-1][j] == 'O' and (m-1, j) not in visited:
                bfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(mn)
    space: O(mn) for hash table <visited>, O(min(m,n)) for <stack>,
        totally, O(mn).
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                board[x][y] = '#'
                for dx, dy in directions:
                    if (
                        0 <= x+dx < m and
                        0 <= y+dy < n and
                        board[x+dx][y+dy] == 'O' and
                        (x+dx, y+dy) not in visited
                    ):
                        stack.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        for i in range(m):
            if board[i][0] == 'O' and (i, 0) not in visited:
                dfs(i, 0)
            if board[i][n-1] == 'O' and (i, n-1) not in visited:
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and (0, j) not in visited:
                dfs(0, j)
            if board[m-1][j] == 'O' and (m-1, j) not in visited:
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
