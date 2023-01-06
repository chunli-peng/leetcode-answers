class Solution:
    """
    Approach 1: Binary Search
    time: O(nlogm), where n=len(piles), m=max(piles)
    space: O(1)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left+right)//2
            time = sum(math.ceil(pile/mid) for pile in piles)
            if time <= h:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        return res
