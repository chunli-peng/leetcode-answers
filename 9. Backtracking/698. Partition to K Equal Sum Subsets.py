class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree + Pruning
    time: O(nlogn) for sort(), O(k^n) for dfs(), totally, O(k^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        n, target = len(nums), sum(nums) // k
        nums.sort(reverse=True)
        visited = set()

        def dfs(i=0, count=0, path=0):
            if count == k-1:  # No need for checking the last subset
                return True
            if target == path:
                return dfs(0, count + 1, 0)

            for j in range(i, n):
                if ((j > 0 and j-1 not in visited and nums[j] == nums[j-1])  # skip in different path
                        or (j in visited or path + nums[j] > target)):  # skip in same path
                    continue  # pruning
                visited.add(j)
                if dfs(j+1, count, path+nums[j]):
                    return True
                visited.remove(j)
            return False
        return dfs()


class Solution:
    """
    unfinished
    Approach 2: Bitwise DFS + Memory Search
    time: O(nlogn) for sort(), O(k^n) for dfs(), totally, O(k^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solutions/1833777/hua-fen-wei-kge-xiang-deng-de-zi-ji-by-l-v66o/
    """
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        n, target = len(nums), sum(nums) // k
        nums.sort(reverse=True)
        visited = set()


class Solution:
    """
    Approach 3: Bitwise DFS + Dynamic Programming
    time: O(nlogn) for sort(), O(k^n) for dfs(), totally, O(k^n)
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        n, target = len(nums), sum(nums) // k
        nums.sort(reverse=True)
        visited = set()