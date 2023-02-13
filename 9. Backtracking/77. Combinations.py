class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(k*C(n,k)), where C(n,k) is Binomial Coefficient.
    space: O(n) for function stack, O(k) for temporary variable <path>,
        totally, O(n)
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # # complete version:
        # def dfs(i=1, path=[]):
        #     if n-i+1 < k-len(path):  # pruning
        #         return
        #     if len(path) == k:
        #         res.append(path.copy())  # or path[:]
        #         return
        #     for j in range(i, n+1):
        #         path.append(j)  # decision to include [j]
        #         dfs(j+1, path)
        #         path.pop()  # decision NOT to include [j]

        # simplified version:
        def dfs(i=1, path=[]):
            if n-i+1 < k-len(path):  # pruning
                return
            if len(path) == k:
                res.append(path)
            for j in range(i, n+1):
                dfs(j+1, path+[j])
        dfs()
        return res


class Solution:
    """
    Approach 2: Alphabet Order
    time: O(k*C(n,k)), where C(n,k) is Binomial Coefficient.
    space: O(n) for function stack, O(k) for temporary variable <path>.
        totally, O(n)
    unfinished
    https://leetcode.cn/problems/combinations/solutions/405094/zu-he-by-leetcode-solution/
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []

        return res