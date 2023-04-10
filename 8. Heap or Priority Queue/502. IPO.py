class Solution:
    """
    Approach 1: Two Heaps
    time: O(n) for heapify() in Python, n tims heappush() with O(logn)
        k times heappop() with O(logn), totally, O((n+k)*logn)
    space: O(n) for heaps
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):  # pruning
            return w + sum(nlargest(k, profits))

        max_profit = []  # only projects we can afford
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)

        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                _, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -1 * p)
            if not max_profit:
                break
            w += -1 * heapq.heappop(max_profit)
        return w
