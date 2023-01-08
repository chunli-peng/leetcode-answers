class Solution:
    """
    Approach 1: Trie + DFS
    time: O(∑n+m), where ∑n is the total number of characters in products, m=len(searchWord).
    space: O(∑n)
    """
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            self.add_word(root, word)

        res = []
        cur = root
        flag = True
        for ch in searchWord:
            if flag and ch in cur.children:
                cur = cur.children[ch]
                res.append(cur.words)
            else:
                res.append([])
                flag = False
        return res

    def add_word(self, root, word):
        cur = root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
            cur.words.append(word)
            cur.words.sort()
            if len(cur.words) > 3:
                cur.words.pop()


class Trie:
    def __init__(self):
        self.children = dict()
        self.words = list()


class Solution:
    """
    Approach 2: Binary Search
    time: O(nlogn+mlogn), where n=len(products), m=len(searchWord),
    O(nlogn) comes from sorting, O(mlogn) comes from binary search.
    space: O(logn) for sorting
    """
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        left, right = 0, len(products)-1
        for i in range(len(searchWord)):
            ch = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != ch):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != ch):
                right -= 1

            res.append([])
            for j in range(min(3, right-left+1)):
                res[-1].append(products[left+j])
        return res
