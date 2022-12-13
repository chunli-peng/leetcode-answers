class Solution:
    """
    Approach 1: Sliding Window + Sorting
    time: O(nlogn), space: O(logn) for sorting
    """
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, sum_wind, len_wind, res = 0, nums[0], 1, 1
        for right in range(1, len(nums)):
            sum_wind += nums[right]
            len_wind += 1
            while k < nums[right]*len_wind-sum_wind:
                sum_wind -= nums[left]
                left += 1
                len_wind -= 1
            res = max(res, len_wind)
        return res
