class Solution:
    """
    Approach 1: Enumeration
    time: O(max(m, n)), space: O(1)
    """
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        board[rMove][cMove] = color

        def check(i, j, di, dj):
            length = 1
            while (0 <= i+di < m and 0 <= j+dj < n):
                length += 1
                if board[i+di][j+dj] == '.':
                    return False
                if board[i+di][j+dj] == color:
                    return length >= 3
                i += di
                j += dj
            return False

        for di, dj in directions:
            if check(rMove, cMove, di, dj):
                return True
        return False
