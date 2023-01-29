class Trie:
    """
    Approach 1: Arrary Implementation
    time: O(1) for initialization, O(|word|) for other functios.
    space: O(n*|Σ|), where Σ is the character set, n is the total length of all words.
    """
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch)-ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch)-ord('a')
            if not node.children[ch]:
                return
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None


class Trie:
    """
    Approach 2: Dictionary Implementation
    time: O(1) for initialization, O(|word|) for other functios.
    space: O(n), n is the total length of all words.
    """
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            if ch not in node.children:
                return
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
