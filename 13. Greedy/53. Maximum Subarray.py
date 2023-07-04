class Solution:
    """
    Approach 1: Dynamic Programing
    time: O(n), space: O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]] + [0] * (n-1)
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


class Solution:
    """
    Approach 1.2: Dynamic Programing (Rolling Array)
    time: O(n), space: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        res, dp = nums[0], 0
        for num in nums:
            dp = max(num, dp+num)
            res = max(res, dp)
        return res


class Solution:
    """
    Approach 2: Greedy
    time: O(n), space: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0:
                total = 0
        return res


class Solution:
    """
    Approach 3: Divide and Conquer
    time: O(logn) for recursion depth,
        visit all nodes with O(Σ(1->logn)2^i) = O(n)
    space: O(logn)
    Follow-up requirement: Divide and Conquer
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_left = self.maxSubArray(nums[0:n//2])
        max_right = self.maxSubArray(nums[n//2:n])

        left = nums[n//2-1]
        tmp = 0
        for i in range(n//2-1, -1, -1):
            tmp += nums[i]
            left = max(tmp, left)

        right = nums[n // 2]
        tmp = 0
        for i in range(n // 2, n):
            tmp += nums[i]
            right = max(tmp, right)
        return max(max_right, max_left, left+right)


class Solution:
    """
    Approach 3.2: Segment Tree
    time: O(logn) for recursion depth,
        visit all nodes with O(Σ(1->logn)2^i) = O(n)
    space: O(logn)
    detail: If we store all status by head, we could find any result with O(logn)
    Follow-up requirement: Divide and Conquer
    """
    class Status:
        def __init__(self, lSum, rSum, mSum, iSum):
            self.lSum = lSum  # max sub array sum from left
            self.rSum = rSum  # max sub array sum from right
            self.mSum = mSum  # max sub array sum
            self.iSum = iSum  # total sum in the interval

    def maxSubArray(self, nums: List[int]) -> int:
        return self._get_info(nums, 0, len(nums)-1).mSum

    def _get_info(self, arr: List[int], left: int, right: int) -> Status:
        if left == right:
            return self.Status(arr[left], arr[left], arr[left], arr[left])
        mid = (left + right) // 2
        lSub = self._get_info(arr, left, mid)
        rSub = self._get_info(arr, mid+1, right)
        return self._push_up(lSub, rSub)

    def _push_up(self, lSub: Status, rSub: Status) -> Status:
        iSum = lSub.iSum + rSub.iSum
        lSum = max(lSub.lSum, lSub.iSum + rSub.lSum)
        rSum = max(rSub.rSum, rSub.iSum + lSub.rSum)
        mSum = max(max(lSub.mSum, rSub.mSum), lSub.rSum + rSub.lSum)
        return self.Status(lSum, rSum, mSum, iSum)