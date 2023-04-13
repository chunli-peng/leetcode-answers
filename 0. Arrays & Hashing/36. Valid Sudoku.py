class Solution:
    """
    Approach 1: Hash Table
    time: O(1), space: O(1), since size of sudoku is fix.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_table = collections.defaultdict(set)  # key = r
        col_table = collections.defaultdict(set)  # key = c
        square_table = collections.defaultdict(set)  # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in row_table[r]
                    or board[r][c] in col_table[c]
                    or board[r][c] in square_table[(r // 3, c // 3)]
                ):
                    return False
                row_table[r].add(board[r][c])
                col_table[c].add(board[r][c])
                square_table[(r // 3, c // 3)].add(board[r][c])
        return True
