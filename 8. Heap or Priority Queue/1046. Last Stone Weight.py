class Solution:
    """
    Approach 1: Max Heap
    time: O(n) for heapify() in Python,
        n times for heappop() with O(logn),
        totally, O(n+nlogn) = O(nlogn).
    space: O(n)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y - x)

        stones.append(0)
        return abs(stones[0])
