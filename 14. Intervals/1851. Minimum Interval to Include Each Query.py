class Solution:
    """
    Approach 1: Min Heap
    time: O(nlogn) for sort(), O(nlogn) for build heap,
        O(logn) for pop() with queries of O(m),
        totally, O((m+n)logn)
    space: O(logn) for sort(), O(n) for <min_heap>, O(m) for hashtable <res>
        totally, O(m+n)
    """
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []  # [(size, right), ...]
        res = {}
        i, n = 0, len(intervals)

        for que in sorted(queries):
            while i < n and intervals[i][0] <= que:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right-left+1, right))
                i += 1

            while min_heap and min_heap[0][1] < que:
                heapq.heappop(min_heap)
            res[que] = min_heap[0][0] if min_heap else -1

        return [res[que] for que in queries]
