class Solution:
    """
    Approach 1: Sorting + Slicing
    time: O(nlogn), space: O(logn) for sorting
    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = [None] * n
        if n % 2 == 1:  # odd
            res[0:n:2], res[1:n:2] = nums[:(n//2+1)], nums[(n//2+1):]
        else:  # even
            res[0:n:2], res[1:n:2] = nums[:(n//2)], nums[(n//2):]
        return res
