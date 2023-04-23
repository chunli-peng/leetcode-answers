class Solution:
    """
    Approach 1: Sort
    time: O(nlogn), space: O(logn)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for left, right in intervals:
            if not res or res[-1][1] < left:
                res.append([left, right])
            else:
                res[-1][1] = max(res[-1][1], right)  # merge
        return res
