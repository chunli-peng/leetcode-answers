class Solution:
    """
    Approach 1: Sliding Window
    time: O(n), space: O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort()
        left, n, sum_wind = 0, len(nums), 0
        res = n + 1
        for right in range(n):
            sum_wind += nums[right]
            while sum_wind >= target:
                res = min(res, right-left+1)
                sum_wind -= nums[left]
                left += 1
        return res if res != n+1 else 0


class Solution:
    """
    Approach 2: Prefix Sum + Binary Search
    time: O(nlogn), space: O(n)
    detail: follow up requirement O(nlogn)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1

        pre_sum = [0]
        for i in range(n):
            pre_sum.append(pre_sum[-1] + nums[i])

        for left in range(1, n + 1):
            right = bisect_left(pre_sum, pre_sum[left-1]+target)
            if right != n+1:
                res = min(res, right-left+1)

        return res if res != n+1 else 0
