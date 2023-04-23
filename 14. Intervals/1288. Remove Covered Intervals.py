class Solution:
    """
    Approach 1: Iteration
    time: O(nlogn) for sort(), space: O(logn) for sort()
    """
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        res, rmax = n, intervals[0][1]

        for i in range(1, n):
            if intervals[i][1] < rmax:
                res -= 1
            else:
                rmax = max(rmax, intervals[i][1])
        return res
