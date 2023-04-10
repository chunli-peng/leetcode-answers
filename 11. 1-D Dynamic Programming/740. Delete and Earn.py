class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n+m), space: O(n+m), where m=max(nums)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        total = [0]*(max_val+1)
        for num in nums:
            total[num] +=num
        return self._rob(total)

    def _rob(self, nums: List[int]) -> int:
        '''Problem 198'''
        n = len(nums)
        dp = [0] + [nums[0]] + [0] * (n-1)
        for i in range(2, n+1):
            # since array <dp> has dummy head, nums[i] should be nums[i-1]
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n+m), space: O(m), where m=max(nums)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        total = [0]*(max_val+1)
        for num in nums:
            total[num] +=num
        return self._rob(total)

    def _rob(self, nums: List[int]) -> int:
        '''Problem 198'''
        n = len(nums)
        prev, curr = 0, nums[0]
        for i in range(1, n):
            prev, curr = curr, max(curr, prev+nums[i])
        return curr


class Solution:
    """
    Approach 2: Sort + Dynamic Programming
    time: O(nlogn+n)=O(nlogn), space: O(n)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        total = [nums[0]]

        for i in range(1, n):
            val = nums[i]
            if val == nums[i - 1]:
                total[-1] += val
            elif val == nums[i - 1] + 1:
                total.append(val)
            else:
                res += self._rob(total)
                total = [val]

        res += self._rob(total)
        return res

    def _rob(self, nums: List[int]) -> int:
        '''Problem 198'''
        n = len(nums)
        dp = [0] + [nums[0]] + [0] * (n-1)
        for i in range(2, n+1):
            # since array <dp> has dummy head, nums[i] should be nums[i-1]
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]


class Solution:
    """
    Approach 2.2: Sort + Dynamic Programming (Rolling Array)
    time: O(nlogn+n)=O(nlogn), space: O(n)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        total = [nums[0]]

        for i in range(1, n):
            val = nums[i]
            if val == nums[i - 1]:
                total[-1] += val
            elif val == nums[i - 1] + 1:
                total.append(val)
            else:
                res += self._rob(total)
                total = [val]

        res += self._rob(total)
        return res

    def _rob(self, nums: List[int]) -> int:
        '''Problem 198'''
        n = len(nums)
        prev, curr = 0, nums[0]
        for i in range(1, n):
            prev, curr = curr, max(curr, prev+nums[i])
        return curr
