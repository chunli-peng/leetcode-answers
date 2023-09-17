"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    """
    Approach 1: Recursive DFS
    time:   T(n)=4T(n/2)+O(n^2), T(1)=O(1),
        from master theorem, we get T(n) = O(logn * n^2)
    space: O(logn) for the recursive stack
    """
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, row, col):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row+i][col+j]:
                        all_same = False
                        break
            if all_same:
                return Node(grid[row][col], True)

            n = n // 2
            top_left = dfs(n, row, col)
            top_right = dfs(n, row, col+n)
            bot_left = dfs(n, row+n, col)
            bot_right = dfs(n, row+n, col+n)
            return Node(0, False, top_left, top_right, bot_left, bot_right)
        return dfs(len(grid), 0, 0)


class Solution:
    """
    Approach 2: Recursive DFS + Prefix Sum
    time:  T(n)=4T(n/2)+O(1), T(1)=O(1),
        from master theorem, we get T(n) = O(n^2)
    space: O(logn) for the recursive stack, O(n^2) for the prefix sum matrix <pre_sum>
    """
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        pre_sum = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + grid[i-1][j-1]

        def get_sum(n, row, col) -> int:
            return pre_sum[row+n][col+n] - pre_sum[row+n][col] - pre_sum[row][col+n] + pre_sum[row][col]

        def dfs(n, row, col):
            sum = get_sum(n, row, col)
            if sum == 0 or sum == n**2:  # all elements are same
              return Node(grid[row][col], True)

            n = n // 2

            top_left = dfs(n, row, col)
            top_right = dfs(n, row, col+n)
            bot_left = dfs(n, row+n, col)
            bot_right = dfs(n, row+n, col+n)
            return Node(0, False, top_left, top_right, bot_left, bot_right)
        return dfs(n, 0, 0)
