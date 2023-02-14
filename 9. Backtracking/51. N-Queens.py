class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(N!), where n is the numbers of Queens
    space: O(N) for function stack, O(n) for hash table <col>, <pos_diag>, <neg_diag>,
        totally, O(n)
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r=0):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        dfs()
        return res


class Solution:
    """
    unfinished
    Approach 2: Bitwise DFS
    time: O(N!), where n is the numbers of Queens
    space: O(N) for function stack, O(n) for hash table <col>, <pos_diag>, <neg_diag>,
        totally, O(n)
        https://leetcode.cn/problems/n-queens/solutions/398929/nhuang-hou-by-leetcode-solution/
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
