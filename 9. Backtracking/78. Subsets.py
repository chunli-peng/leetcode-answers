class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(2^n) for dfs(), O(n) for append(), totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <subset>,
        totally, O(n)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        # # complete version:
        # def dfs(i=0, subset=[]):
        #     res.append(subset.copy())  # or subset[:]
        #     for j in range(i, n):
        #         subset.append(nums[j])  # decision to include nums[j]
        #         dfs(j+1, subset)
        #         subset.pop()  # decision NOT to include nums[j]

        # simplified version:
        def dfs(i=0, subset=[]):
            res.append(subset)  # No need for copy operations
            for j in range(i, n):
                dfs(j+1, subset + [nums[j]])
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS in Binary Tree
    time: O(2^n) for dfs(), O(n) for append(), totally, O(n*2^n)
    space: O(n) for function stack, O(n) for temporary variable <subset>,
        totally, O(n)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        # # complete version:
        # def dfs(i=0, subset=[]):
        #     if i == n:
        #         res.append(subset.copy())  # or subset[:]
        #         return
        #     subset.append(nums[i])  # decision to include nums[i]
        #     dfs(i+1, subset)
        #     subset.pop()  # decision NOT to include nums[i]
        #     dfs(i+1, subset)

        # simplified version:
        def dfs(i=0, subset=[]):
            if i == n:
                res.append(subset)  # No need for copy operations
                return
            dfs(i+1, subset+[nums[i]])  # decision to include nums[i]
            dfs(i+1, subset)  # decision NOT to include nums[i]
        dfs()
        return res


class Solution:
    """
    Approach 2: Iteration
    time: O(n*2^n)
    space: O(n) for temporary variable <subset>
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
