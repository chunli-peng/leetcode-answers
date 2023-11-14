class Solution:
    """
    Approach 1: Min Heap
    time: O(nlogM + nlogn) for creating the heap, where M=max(nums),
        O(n*logn*logM) for heappop() and heappush(), totally, O(n*logM*logn)
    space: O(n)
    """
    def minimumDeviation(self, nums: List[int]) -> int:
        min_heap = []  # [(num, the cap of num)]
        heap_cap = 0  # the maximum of the heap
        res = float('inf')

        # O(nlogM)
        for num in nums:
            temp = num
            while num % 2 == 0:
                num //= 2
            min_heap.append((num, max(num * 2, temp)))
            heap_cap = max(heap_cap, num)

        # O(nlogn)
        heapq.heapify(min_heap)

        # O(n*logn*logM)
        while len(min_heap) == len(nums):
            num, n_max = heapq.heappop(min_heap)
            res = min(res, heap_cap-num)
            if num < n_max:
                heapq.heappush(min_heap, (num*2, n_max))
                heap_cap = max(heap_cap, num*2)
        return res
