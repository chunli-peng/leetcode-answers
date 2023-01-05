class Solution:
    """
    Approach 1: Binary Search
    time: O(logn), space: O(1)
    """
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        res = 0
        while left <= right:
            mid = (left+right)//2
            coins = (1+mid)*mid/2
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(mid, res)
        return res


class Solution:
    """
    Approach 2: Math
    time: O(1), space: O(1)
    detail: Solve the Equation (1+x)*x/2 = n
    """
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)  # quadratic formula
