class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(nlogn) for sort(), O(2^n) for dfs(), O(n) for append(),
        totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        candidates.sort()
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if sum(path) > target:  # pruning
        #         return
        #     if sum(path) == target:
        #         res.append(path.copy())  # or path[:]
        #     for j in range(i, n):
        #         if j != i and candidates[j] == candidates[j-1]:
        #             continue
        #         path.append(candidates[j])  # decision to include candidates[j]
        #         dfs(j+1, path)
        #         path.pop()  # decision NOT to include candidates[j]

        # simplified version:
        def dfs(i=0, path=[]):
            if sum(path) > target:  # pruning
                return
            if sum(path) == target:
                res.append(path)
            for j in range(i, n):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                dfs(j+1, path + [candidates[j]])
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS in Binary Tree
    time: O(nlogn) for sort(), O(2^n) for dfs(), O(n) for append(),
        totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        candidates.sort()
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if target == sum(path):
        #         res.append(path.copy())  # or path[:]
        #         return
        #     if i == n or sum(path) > target:  # pruning
        #         return
        #     path.append(candidates[i])  # decision to include candidates[i]
        #     dfs(i+1, path)
        #     path.pop()  # decision NOT to include candidates[i]
        #     while i != n-1 and candidates[i] == candidates[i+1]:
        #         i += 1  # choose unduplicated number
        #     dfs(i+1, path)

        # simplified version:
        def dfs(i=0, path=[]):
            if target == sum(path):
                res.append(path)  # No need for copy operations
                return
            if i == n or sum(path) > target:  # pruning
                return
            dfs(i+1, path+[candidates[i]])
            while i != n-1 and candidates[i] == candidates[i+1]:
                i += 1  # choose unduplicated number
            dfs(i+1, path)
        dfs()
        return res


class Solution:
    """
    Approach 2: Recursive DFS in Multiway Tree by Counter
    time: O(n) for Counter(), O(2^n) for dfs(), O(n) for append(),
        totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = sorted(collections.Counter(candidates).items())
        res, n = [], len(counts)

        def dfs(i=0, rest=target, path=[]):
            if not rest:
                res.append(path)
                return
            if i == n or rest < counts[i][0]:
                return

            num, freq = counts[i][0], counts[i][1]
            upper = min(rest // num, freq)  # upper bound
            for j in range(0, upper+1):
                dfs(i+1, rest-j*num, path+j*[num])
        dfs()
        return res
