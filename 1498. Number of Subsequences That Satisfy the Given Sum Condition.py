class Solution:
    """
    Approach 1: Binary Search + Sorting
    time: O(nlogn), space: O(n)
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        sol = 0

        n = len(nums)
        max_val = 10**9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % max_val

        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            threshold = target - num
            index = bisect.bisect_right(nums, threshold) - 1
            contribute = f[index - i] if index >= i else 0
            sol += contribute

        return sol % max_val
