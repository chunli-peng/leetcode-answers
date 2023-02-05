class Solution:
    """
    Approach 1: Trie + DFS
    time: O(n) for initialization of the Trie
        O(m*n*3^k) for findWords(), where k is max length of word.
    space: O(n), n is the total length of all words.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)  # Build the trie

        m, n, res = len(board), len(board[0]), []

        def dfs(i=0, j=0, node=root):
            ch = board[i][j]
            if ch not in node.children:
                return

            node = node.children[ch]
            if node.is_end:
                node.is_end = False
                res.append(node.word)

            board[i][j] = '#'  # Revise temporarily for recording visited point
            for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= new_i < m and 0 <= new_j < n:
                    dfs(new_i, new_j, node)
            board[i][j] = ch  # Restore
            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
        self.word = None

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True
        node.word = word


class Solution:
    """
    Approach 1.2: Trie + DFS (delete visited words)
    time: O(n) for initialization of the Trie
        O(m*n*3^k) for findWords(), where k is max length of word.
    space: O(n), n is the total length of all words.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)  # Build the trie

        m, n, res = len(board), len(board[0]), []

        def dfs(i=0, j=0, node=root):
            ch = board[i][j]
            if ch not in node.children:
                return

            nxt = node.children[ch]
            if nxt.is_end:
                nxt.is_end = False
                res.append(nxt.word)
                nxt.word = None  # Delete the visited word

            if nxt.children:
                board[i][j] = '#'  # Revise temporarily for recording visited point
                for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < m and 0 <= new_j < n:
                        dfs(new_i, new_j, nxt)
                board[i][j] = ch  # Restore
            else:
                node.children.pop(ch)  # Delete the empty node
            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
        self.word = None

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True
        node.word = word
