class Solution:
    """
    Approach 1: Dynamic Programming + Hash Table
    time: O(n^2), space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        hashtable = set(wordDict)
        dp = [True] + [False] * n
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in hashtable):
                    dp[j] = True
        return dp[-1]


class Solution:
    """
    Approach 1.2: Dynamic Programming + Hash Table (alternative code)
    time: O(n^2), space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]  # indices of viable segmentation
        hashtable = set(wordDict)
        for j in range(0, n+1):
            for i in dp:
                if s[i:j] in hashtable:
                    dp.append(j)
                    break
        return dp[-1] == n


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(n^2), space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        len_list = [len(word) for word in wordDict]
        max_len, min_len = max(len_list), min(len_list)
        cache = {}

        def dfs(s=s):
            if s in cache:
                return cache[s]
            if len(s) == 0:
                cache[s] = True
                return True
            if len(s) < min_len:
                cache[s] = False
                return False
            for i in range(min_len, min(max_len, len(s)) + 1):
                if s[:i] in wordDict and dfs(s[i:]):
                    cache[s] = True
                    return True
            cache[s] = False
            return False
        return dfs()


class Solution:
    """
    Approach 2.2: Recursive DFS + Memory Search (Built-in Func)
    time: O(n^2), space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        len_list = [len(word) for word in wordDict]
        max_len, min_len = max(len_list), min(len_list)

        @cache
        def dfs(s=s):
            if len(s) == 0:
                return True
            if len(s) < min_len:
                return False
            for i in range(min_len, min(max_len, len(s)) + 1):
                if s[:i] in wordDict and dfs(s[i:]):
                    return True
            return False
        return dfs()


class Solution:
    """
    unfinished
    Approach 3: Trie
    time: O(n^2), space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
