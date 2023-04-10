class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp)


class Solution:
    """
    Approach 2: Greedy + Binary Search
    time: O(nlogn), space: O(n)
    Follow-up requirement: time: O(nlog(n))
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:  # find the location by binary search
                left, right = 0, len(res)-1
                loc = right  # location of replacement
                while left <= right:
                    mid = (left+right)//2
                    if num <= res[mid]:
                        right = mid - 1
                        loc = mid
                    else:
                        left = mid + 1
                res[loc] = num
        return len(res)
