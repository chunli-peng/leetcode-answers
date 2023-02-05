class SeatManager:
    """
    Approach 1: Min Heap
    time: O(n) for __init__(), O(logn) for reserve(), unreserve(),
    space: O(n)
    """
    def __init__(self, n: int):
        self.available = list(range(1, n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
