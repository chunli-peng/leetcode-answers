class Solution:
    """
    Approach 1: Brute Force
    time: O(n^2) for dfs(), space: O(n)
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res, n = 0, len(nums)
        hash_table = {int(num, 2) for num in nums}
        while res in hash_table:
            res += 1
        res = "{:b}".format(res)
        return '0' * (n-len(res)) + res


class Solution:
    """
    Approach 2: Recursive DFS in Multiway Tree
    time: O(n^2) for dfs(), space: O(n)
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res, n = None, len(nums)
        hash_table = set(nums)

        def dfs(i=0, path=['0']*n):
            nonlocal res
            if i == n and ''.join(path) not in hash_table:
                res = ''.join(path)
                return
            for j in range(i, n):
                if ''.join(path) in hash_table:
                    path[j] = '1'
                    dfs(j+1, path)
                    path[j] = '0'
                else:
                    res = ''.join(path)
                    return
        dfs()
        return res



class Solution:
    """
    Approach 3: Recursive DFS in Binary Tree
    time: O(n^2) for dfs(), space: O(n)
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        hash_table = set(nums)

        def dfs(i=0, path='0'*n):
            if i == n:
                return path if path not in hash_table else None
            res = dfs(i+1, path)
            if res:
                return res
            res = dfs(i+1, path[:i]+'1'+path[i+1:])
            if res:
                return res
        return dfs()


class Solution:
    """
    Approach 4: Recursion (Math: Cantor's diagonal)
    time: O(n) for dfs(), space: O(n)
    detail: since the solution always exists, there is no need for search all space.
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        hash_table = set(nums)

        def helper(i=0, path='0'*n):
            if path not in hash_table:
                return path
            return helper(i+1, path[:i]+'1'+path[i+1:])
        return helper()


class Solution:
    """
    Approach 5: Iteration (Math: Cantor's diagonal)
    time: O(n), space: O(n)
    detail: since the solution always exists, there is no need for search all space.
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i, num in enumerate(nums):
            if num[i] == '1':
                res.append('0')
            else:
                res.append('1')
        return ''.join(res)
