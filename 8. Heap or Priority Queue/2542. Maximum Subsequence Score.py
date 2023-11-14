class Solution:
    """
    Approach 1: Min Heap
    time: O(nlogn) for sorted(), O(nlogk) for heappush(),
        O((n-k)*logk) for heappop(), totally, O(nlogn)
    space: O(n)
    """
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        min_heap = []
        sum_n1 = 0
        res = 0

        for n1, n2 in pairs:
            heapq.heappush(min_heap, n1)
            sum_n1 += n1

            if len(min_heap) > k:
                sum_n1 -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                res = max(res, sum_n1*n2)
        return res
