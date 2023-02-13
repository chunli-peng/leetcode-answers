class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree by State Variable
    time: O(n*n!)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        O(n) for state variable <visited>, totally, O(n)
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        nums.sort()
        visited = [False] * n

        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
            for j in range(n):
                if not visited[j]:
                    # nums[j] and nums[j-1] in one path when visited[j-1]=True
                    if j > 0 and nums[j] == nums[j-1] and not visited[j-1]:
                        continue
                    visited[j] = True
                    dfs(i+1, path+[nums[j]])
                    visited[j] = False
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS by Counter
    time: O(n) for Counter(), O(n*n!) for dfs(),
        totally, O(n*n!)
    space: O(n) for function stack, O(n) for temporary variable <path>, 
        totally, O(n)
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        counts = collections.Counter(nums)

        def dfs(i=0, path=[]):
            if i == n:
                res.append(path)
            for num in counts:
                if counts[num] == 0:
                    continue
                counts[num] -= 1
                dfs(i+1, path+[num])
                counts[num] += 1
        dfs()
        return res
