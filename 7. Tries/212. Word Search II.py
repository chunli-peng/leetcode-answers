class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)  # Build the trie

        m, n = len(board), len(board[0])
        res = set()  # Remove duplicates
        visited = set()  # Record the visited points

        def dfs(i=0, j=0, node=root, word=''):
            ch = board[i][j]
            if (i, j) in visited or ch not in node.children:
                return
            visited.add((i, j))
            node = node.children[ch]
            word += ch
            if node.is_end:
                node.is_end = False
                res.add(word)
            for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    dfs(new_i, new_j, node, word)
            visited.remove((i, j))
            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return list(res)


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True
