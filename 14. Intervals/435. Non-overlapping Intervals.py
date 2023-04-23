class Solution:
    """
    Approach 1: Greedy
    time: O(nlogn) for sort(), space: O(logn) for sort()
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        pre_end = intervals[0][1]
        for left, right in intervals[1:]:
            if left >= pre_end:
                pre_end = right
            else:
                res += 1
                pre_end = min(pre_end, right)
        return res
