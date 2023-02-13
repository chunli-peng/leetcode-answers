class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(mn*3^L), where L is the word length, without considering pruning
    space: O(mn) for hash set <seen>, O(min(L,mn)) for function stack,
        totally, O(mn)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, length = len(board), len(board[0]), len(word)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        path = set()  # store visited points

        def dfs(i, j, k=0):
            if board[i][j] != word[k]:
                return False
            if k == length-1:
                return True

            path.add((i, j))
            for (di, dj) in directions:
                new_i, new_j = i+di, j+dj
                if (
                    0 <= new_i < rows and 0 <= new_j < cols and
                    (new_i, new_j) not in path and
                    dfs(new_i, new_j, k+1)
                ):
                    return True
            path.remove((i, j))  # back
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):
                    return True
        return False


class Solution:
    """
    Approach 1.2: Recursive DFS in Multiway Tree by Pruning
    time: O(mn*3^L), where L is the word length, without considering pruning
    space: O(mn) for hash set <seen>, O(min(L,mn)) for function stack,
        totally, O(mn)
    Follow-up requirement: use search pruning
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, length = len(board), len(board[0]), len(word)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        path = set()  # store visited points

        def dfs(i, j, k=0):
            if board[i][j] != word[k]:
                return False
            if k == length-1:
                return True

            path.add((i, j))
            for (di, dj) in directions:
                new_i, new_j = i+di, j+dj
                if (
                    0 <= new_i < rows and 0 <= new_j < cols and
                    (new_i, new_j) not in path and
                    dfs(new_i, new_j, k+1)
                ):
                    return True
            path.remove((i, j))  # back
            return False

        # reverse the word if frequency of the first letter is`\
        # more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):
                    return True
        return False
