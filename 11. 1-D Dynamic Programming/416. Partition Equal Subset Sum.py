class Solution:
    """
    Approach 1: 2-D Dynamic Programming
    time: O(n*target), space: O(n*target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        target = total // 2
        if (
            n < 2 or
            total % 2 != 0 or  # odd number
            max(nums) > target  # avoid index out of range
        ):
            return False

        dp = [[False]*(target+1) for _ in range(n)]
        dp[0][0], dp[0][nums[0]] = True, True

        for i in range(1, n):
            for j in range(target+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]


class Solution:
    """
    Approach 1.2: 1-D Dynamic Programming (Rolling Array: O(2*target))
    time: O(n*target), space: O(target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        target = total // 2
        if (
            n < 2 or
            total % 2 != 0  # odd number
        ):
            return False

        prev = [True] + [False] * target
        curr = prev[:]

        for num in nums:
            for j in range(num, target+1):
                curr[j] = prev[j] | prev[j-num]
            prev = curr[:]
            if prev[target]:  # pruning
                return True
        return False


class Solution:
    """
    Approach 1.3: 1-D Dynamic Programming (Rolling Array: O(target))
    time: O(n*target), space: O(target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        target = total // 2
        if (
            n < 2 or
            total % 2 != 0  # odd number
        ):
            return False

        dp = [True] + [False] * target

        for num in nums:
            # reverse update: use the last state of dp[j-num]
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]
            if dp[target]:  # pruning
                return True
        return False


class Solution:
    """
    Approach 1.4: 1-D Dynamic Programming by Hash Table
    time: O(n*target), space: O(target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        dp = set([0])
        for num in nums:
            temp = set()
            for j in dp:
                if j+num == target:
                    return True
                if j+num < target:
                    temp.add(j+num)
                temp.add(j)
            dp = temp
        return False


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(2^n), space: O(n)
    """
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        @cache
        def dfs(i=0, cur_sum=0):
            if cur_sum == target:
                return True
            if i == len(nums) or cur_sum > target:
                return False
            return dfs(i+1, cur_sum) or dfs(i+1, cur_sum+nums[i])
        return dfs()
