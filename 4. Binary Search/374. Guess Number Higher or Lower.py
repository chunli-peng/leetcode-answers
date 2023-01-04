# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
    Approach 1: Binary Search
    time:O(logn), space: O(1)
    """
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
            else:
                return mid
