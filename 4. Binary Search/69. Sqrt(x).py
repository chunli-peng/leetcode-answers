class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    """
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        res , left , right  = 0, 0, x
        while left < right :
            mid =  (left + right) // 2
            if mid**2 <= x:
                res = mid
                left = mid + 1
            elif mid**2 > x:
                right = mid
        return res
