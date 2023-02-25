class Solution:
    """
    Approach 1: BFS + Hash Table
    time: O(n^2)
    space: O(n^2) for hash table <visited>, O(n) for <queue>,
        totally, O(n^2).
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        visited = set()
        res = 1

        queue = [(0, 0)]
        visited.add((0, 0))
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                if (x, y) == (n-1, n-1):
                    return res
                for dx, dy in directions:
                    if (
                        0 <= x+dx < n and
                        0 <= y+dy < n and
                        grid[x+dx][y+dy] == 0 and
                        (x+dx, y+dy) not in visited
                    ):
                        queue.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            res += 1
        return -1


class Solution:
    """
    unfinished
    Approach 2: A*
    https://leetcode.cn/problems/shortest-path-in-binary-matrix/solutions/1149240/bfsa-qi-fa-sou-suo-duo-chong-fang-fa-you-jrqp/
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: