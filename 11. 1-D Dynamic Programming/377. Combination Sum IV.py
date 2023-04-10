class Solution:
    """
    Approach 1: Recursive DFS + Memory Search
    time: O(n!), space: O(n) for function stack, O(m) for <cache>, where m=target
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(path=0):
            if path == target:
                return 1
            if path > target:
                return 0
            if path in cache:
                return cache[path]
            cache[path] = 0
            for num in nums:
                cache[path] += dfs(path+num)
            return cache[path]
        return dfs()


class Solution:
    """
    Approach 2: Dynamic Programming
    time: O(m*n), space: O(m), where m=m
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target

        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[-1]


"""
Follow-up questions:
    Q: What if negative numbers are allowed in the given array? How does it change the problem?
        A: If negative numbers are allowed, the permutaion array might be infinite, \
        for example, [-5, 5, -5, 5, ...]
    Q: What limitation we need to add to the question to allow negative numbers?
        A: We need to limit the length of the permutation array.
"""
