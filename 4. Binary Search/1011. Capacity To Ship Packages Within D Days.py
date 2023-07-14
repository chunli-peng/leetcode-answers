class Solution:
    """
    Approach 1: Binary Search
    time: O(nlogΣ), where Σ=sum(weights),
    space: O(1)
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def check(capacity):
            counts, cur_cap = 1, capacity
            for w in weights:
                if cur_cap < w:
                    cur_cap = capacity
                    counts += 1
                cur_cap -= w
            return counts <= days

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
