class Solution:
    """
    Approach 1: BFS + Hash Table
    time: O(n^2)
    space: O(n^2) for hash table <visited>, O(n^2) for <queue>,
        totally, O(n^2).
    """
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()

        queue = [(1, 0)]  # pair: (index, moves)
        while queue:
            cur, res = queue.pop(0)
            for i in range(1, 7):
                nex = cur + i
                if nex > n**2:
                    break
                row, col = self._index_to_coord(nex, n)
                if board[row][col] != -1:
                    nex = board[row][col]
                if nex == n**2:
                    return res + 1
                if nex not in visited:
                    visited.add(nex)
                    queue.append((nex, res+1))
        return -1

    def _index_to_coord(self, index, n):
        """Translate the index to coordinates."""
        row = (index-1) // n
        col = (index-1) % n
        if row % 2:
            col = n-1-col
        row = n-1-row
        return (row, col)
