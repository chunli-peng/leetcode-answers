class WordDictionary:
    """
    Approach 1: Arrary + DFS
    time: O(1) for initialization, O(|word|) for addWord(),
            O(|Σ|^n) for search() if each character is '.'.
    space: O(n*|Σ|), where Σ is the character set, n is the total length of all words.
    """
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch)-ord('a')
            if not node.children[ch]:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i=0, node=self) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch != '.':
                child = node.children[ord(ch)-ord('a')]
                if child and dfs(i+1, child):
                    return True
            else:
                for child in node.children:
                    if child and dfs(i+1, child):
                        return True
            return False
        return dfs()


class WordDictionary:
    """
    Approach 2: Dictionary + DFS
    time: O(1) for initialization, O(|word|) for addWord(),
        O(|Σ|^n) for search() if each character is '.', \
            where Σ is the character set.
    space: O(n), n is the total length of all words.
    """
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i=0, node=self) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch != '.':
                if ch in node.children and dfs(i+1, node.children[ch]):
                    return True
            else:
                for child in node.children:
                    if child and dfs(i+1, node.children[child]):
                        return True
            return False
        return dfs()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
