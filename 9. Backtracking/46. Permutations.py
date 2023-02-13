class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree by Swap
    time: O(n*n!), space: O(n) for function stack
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def dfs(i=0):
            if i == n:
                res.append(nums.copy())  # or nums[:]
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]  # back
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS in Multiway Tree by Queue
    time: O(n*n!)
    space: O(n) for function stack, O(n) for temporary variable <subset>.
        totally, O(n)
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:  # base case
            return [nums.copy()]  # or nums[:]

        res = []
        for _ in range(len(nums)):
            num = nums.pop(0)
            subset = self.permute(nums)

            for comb in subset:
                comb.append(num)
            res.extend(subset)
            nums.append(num)
        return res


class Solution:
    """
    Approach 1.3: Recursive DFS in Multiway Tree by State Variable
    time: O(n*n!)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        O(n) for bool variable list: visited.
        totally, O(n)
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        visited = [False] * n

        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    dfs(i+1, path+[nums[j]])
                    visited[j] = False
        dfs()
        return res
