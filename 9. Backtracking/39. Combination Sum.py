class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(2^n) for dfs(), O(n) for append(), totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if sum(path) > target:  # pruning
        #         return
        #     if sum(path) == target:
        #         res.append(path.copy())  # or path[:]
        #     for j in range(i, n):
        #         path.append(candidates[j])  # decision to include candidates[j]
        #         dfs(j, path)
        #         path.pop()  # decision NOT to include candidates[j]

        # simplified version:
        def dfs(i=0, path=[]):
            if sum(path) > target:  # pruning
                return
            if sum(path) == target:
                res.append(path)
            for j in range(i, n):
                dfs(j, path + [candidates[j]])
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS in Binary Tree
    time: O(2^n) for dfs(), O(n) for append(), totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if target == sum(path):
        #         res.append(path.copy())  # or path[:]
        #         return
        #     if i == n or sum(path) > target:  # pruning
        #         return
        #     path.append(candidates[i])  # decision to include candidates[i]
        #     dfs(i, path)  # could choose same element
        #     path.pop()  # decision NOT to include candidates[i]
        #     dfs(i+1, path)

        # simplified version:
        def dfs(i=0, path=[]):
            if target == sum(path):
                res.append(path)  # No need for copy operations
                return
            if i == n or sum(path) > target:  # pruning
                return
            dfs(i, path+[candidates[i]])  # could choose same element
            dfs(i+1, path)
        dfs()
        return res


class Solution:
    """
    Approach 2: Dynamic Programming
    time: O(m*n), space: O(m*n), where m=target
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[[]]] + [[] for _ in range(1, target+1)]
        for num in candidates:
            for i in range(1, target+1):
                if i-num >= 0:
                    for pre_comb in dp[i-num]:
                        dp[i].append(pre_comb+[num])
        return dp[-1]
