class KthLargest:
    """
    Approach 1: Min Heap
    time: O(n) for heapify() in Python,
        n-k times for heappop() with O(logn),
        totally, O((n-k)logn) for the initialization;
        O(logk) for add().
    space: O(n) for the initialization.
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
