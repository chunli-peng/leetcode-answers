class Solution:
    """
    Approach 1: Prefix Sum
    time: O(n), space: O(n)
    Requirement: time: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [None] * n

        prefix, suffix = [1] + [None]*(n-1), [None]*(n-1) + [1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-1-i] = suffix[n-i] * nums[n-i]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]
        return answer


class Solution:
    """
    Approach 1.2: Prefix Sum (Rolling Array)
    time: O(n), space: O(1)
    Requirement: time: O(n)
    Follow-up requirement: space: O(1)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [None] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
