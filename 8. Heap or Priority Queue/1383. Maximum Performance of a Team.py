class Solution:
    """
    Approach 1: Min Heap
    time: O(nlogn) for sort(), O(nlogk) for heappush(),
        O((n-k)*logk) for heappop(), totally, O(nlogn)
    space: O(n)
    """
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        staffs = list(zip(efficiency, speed))
        staffs.sort(reverse=True)
        min_heap, sum_speed, res = [], 0, 0

        for eff, spd in staffs:
            if len(min_heap) == k:
                if spd <= min_heap[0]:  # pruning
                    continue
                sum_speed -= heapq.heappop(min_heap)
            sum_speed += spd
            heapq.heappush(min_heap, spd)
            res = max(sum_speed*eff, res)
        return res % MOD
