class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(n) for check palindrome, O(2^n) for dfs(), since there is 2*(n-1) \
        kinds of partion, totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def partition(self, s: str) -> List[List[str]]:
        res, n = [], len(s)
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if i == n:
        #         res.append(path.copy())  # or path[:]
        #         return
        #     for j in range(i, n):
        #         if self._check(s, i, j):
        #             path.append(s[i:j+1])
        #             dfs(j+1, path)
        #             path.pop()

        # simplified version:
        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
                return
            for j in range(i, n):
                if self._check(s, i, j):
                    dfs(j+1, path+[s[i:j+1]])
        dfs()
        return res

    def _check(self, s, i, j):
        """Check s[i:j+1] is palindrome or not"""
        if i > j:
            return True
        return self._check(s, i+1, j-1) if s[i] == s[j] else False



class Solution:
    """
    Approach 1.2: Recursive DFS + Memory Search
    time: O(n) for check palindrome, O(2^n) for dfs(), since there is 2*(n-1) \
        kinds of partion, totally, O(n*2^n)
    space: O(n^2) for the cache, O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n^2)
    """
    def __init__(self) -> None:
        self.cache = {}  # {(i, j): bool}

    def partition(self, s: str) -> List[List[str]]:
        res, n = [], len(s)

        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
            for j in range(i, n):
                if self._check(s, i, j):
                    dfs(j+1, path+[s[i:j+1]])
        dfs()
        return res

    def _check(self, s, i, j):
        """Check s[i:j+1] is palindrome or not and add to cache"""
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i >= j:
            self.cache[(i, j)] = True
            return True
        if s[i] == s[j]:
            return self._check(s, i+1, j-1)
        else:
            self.cache[(i, j)] = False
            return False

    # # Built-in decorator: cache
    # @cache
    # def _check(self, s, i, j):
    #     """Check s[i:j+1] is palindrome or not"""
    #     if i > j:
    #         return True
    #     return self._check(s, i+1, j-1) if s[i] == s[j] else False


class Solution:
    """
    Approach 2: Recursive DFS + Dynamic Programming (Pretreatment)
    time: O(n) for check palindrome, O(2^n) for dfs(), since there is 2*(n-1) \
        kinds of partion, totally, O(n*2^n)
    space: O(n^2) for dynamic programming, O(n) for function stack,
        O(n) for temporary variable <path>, totally, O(n^2)
    """
    def partition(self, s: str) -> List[List[str]]:
        res, n = [], len(s)
        dp = self._get_palindrome_states(s, n)

        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
            for j in range(i, n):
                if dp[i][j]:
                    dfs(j+1, path+[s[i:j+1]])
        dfs()
        return res

    def _get_palindrome_states(self, s, n):
        """Generate and return palindrome state variable"""
        dp = [[True] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        return dp
