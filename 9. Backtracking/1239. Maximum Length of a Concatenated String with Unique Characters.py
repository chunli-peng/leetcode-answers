class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(nlogn) for sort(), O(2^n) for dfs(), totally, O(2^n)
    space: O(n)
    """
    def maxLength(self, arr: List[str]) -> int:
        res, n = 0, len(arr)
        arr.sort(reverse=True)

        def dfs(i=0, path=''):
            nonlocal res
            res = max(res, len(path))
            hash_table = set(path)
            if i == n:
                return
            if len(path) + sum([len(arr[x]) for x in range(i, n)]) < res:  # pruning
                return
            for j in range(i, n):
                if len(set(arr[j])) == len(arr[j]) \
                        and all(ch not in hash_table for ch in arr[j]):
                    dfs(j+1, path+arr[j])
        dfs()
        return res


class Solution:
    """
    unfinished
    Approach 2: Bit Manipulation
    time: O(2^n) for dfs(), space: O(n)
    https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solutions/834267/chuan-lian-zi-fu-chuan-de-zui-da-chang-d-g6gk/
    """
    def maxLength(self, arr: List[str]) -> int:
        res, n = 0, len(arr)
