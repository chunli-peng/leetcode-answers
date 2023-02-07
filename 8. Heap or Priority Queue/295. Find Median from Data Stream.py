class MedianFinder:
    """
    Approach 1: Two Heaps
    time: O(logn) for addNum(), O(1) for findMedian()
    space: O(n)
    """
    def __init__(self):
        self.min_heap, self.max_heap = [], []  # large, small

    def addNum(self, num: int) -> None:
        if self.max_heap and num < -1*self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-1*self.max_heap[0]+self.min_heap[0])/2
        else:
            return self.min_heap[0]


from sortedcontainers import SortedList
class MedianFinder:
    """
    Approach 2: Sorted Set + Two Pointers
    time: O(logn) for addNum(), O(1) for findMedian()
    space: O(n)
    """
    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        k = n // 2
        if n % 2:  # odd
            return self.nums[k]
        return (self.nums[k-1] + self.nums[k]) / 2  # even


from sortedcontainers import SortedList
class MedianFinder:
    """
    Approach 2.2: Sorted Set + Two Pointers
    time: O(logn) for addNum(), O(1) for findMedian()
    space: O(n)
    """
    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_val = self.right_val = None

    def addNum(self, num: int) -> None:
        n = len(self.nums)
        self.nums.add(num)

        if not n:
            self.left = self.right = 0
        else:
            if num < self.left_val:
                self.left += 1
            if num < self.right_val:
                self.right += 1

            if n & 1:  # odd array -> even array
                if num < self.left_val:
                    self.left -= 1
                else:
                    self.right += 1
            else:  # even array -> odd array
                if self.left_val < num < self.right_val:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_val:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right  # if self.left = num

        self.left_val = self.nums[self.left]
        self.right_val = self.nums[self.right]

    def findMedian(self) -> float:
        return (self.left_val + self.right_val) / 2


from sortedcontainers import SortedList
class MedianFinder:
    """
    Approach 2: Sorted Set + Two Pointers
    time: O(logn) for addNum(), O(1) for findMedian()
    space: O(n)
    Follow-up requirement: If 99% of all integer numbers from the stream \
        are in the range [0, 100], how would you optimize your solution?
    unfinished
    """

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
