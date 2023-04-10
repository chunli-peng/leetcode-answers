class Solution:
    """
    Approach 1: Concatenation
    time: O(n), space: O(1)
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


class Solution:
    """
    Approach 1: Iteration
    time: O(n), space: O(1)
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[i % n] for i in range(2*n)]
