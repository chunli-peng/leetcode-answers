class Solution:
    """
    Approach 1: Sorting
    time: O(nlogn), space: O(logn)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]


class Solution:
    """
    Approach 2: Max Heap
    time: O(n) for heapify() in Python, O(nlogk) for adjust
    space: O(k)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(max_heap)

        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(max_heap, (dist, i))

        res = [points[i] for (_, i) in max_heap]
        return res


class Solution:
    """
    Approach 2.2: Max Heap (user-defined func)
    time: O(klogk) for building a heap, O((n-k)logk) for pushing,
        totally, O(nlogk)
    space: O(1)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        # build the min heap with size of k
        self._max_heapify(points, 0, k)

        # push the remains to the heap
        for i in range(k, n):
            if self._dis(points[i]) < self._dis(points[0]):
                points[i], points[0] = points[0], points[i]
                self._max_heappop(points, 0, k)
        return points[:k]

    def _max_heapify(self, heap, root, heap_len):
        """Build a min heap."""
        for i in range(heap_len-1, -1, root-1):
            self._max_heappop(heap, i, heap_len)

    def _max_heappop(self, heap, root, heap_len):
        """Pop the minimum to the top of heap."""
        cur = root
        while cur*2+1 < heap_len:
            left, right = cur*2+1, cur*2+2
            if heap_len <= right or self._dis(heap[left]) > self._dis(heap[right]):
                nex = left
            else:
                nex = right
            if self._dis(heap[cur]) < self._dis(heap[nex]):
                heap[cur], heap[nex] = heap[nex], heap[cur]
                cur = nex
            else:
                break

    def _dis(self, pair) -> int:
        """Return the square of Euclidean distance"""
        return pair[0]**2 + pair[1]**2


class Solution:
    """
    Approach 2.3: Max Heap (user-defined func)
    detail: save time by store the distances in the stack
    time: O(klogk) for building a heap, O((n-k)logk) for pushing,
        totally, O(nlogk)
    space: O(k)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        max_heap = [(x ** 2 + y ** 2, [x, y]) for i, (x, y) in enumerate(points[:k])]

        # build the min heap with size of k
        self._max_heapify(max_heap, 0, k)

        # push the remains to the heap
        for i in range(k, n):
            if self._dis(points[i]) < max_heap[0][0]:
                max_heap[0] = (self._dis(points[i]), points[i])
                self._max_heappop(max_heap, 0, k)
        return [item[1] for item in max_heap]

    def _max_heapify(self, heap, root, heap_len):
        """Build a min heap."""
        for i in range(heap_len-1, -1, root-1):
            self._max_heappop(heap, i, heap_len)

    def _max_heappop(self, heap, root, heap_len):
        """Pop the minimum to the top of heap."""
        cur = root
        while cur*2+1 < heap_len:
            left, right = cur*2+1, cur*2+2
            if heap_len <= right or heap[left][0] > heap[right][0]:
                nex = left
            else:
                nex = right
            if heap[cur][0] < heap[nex][0]:
                heap[cur], heap[nex] = heap[nex], heap[cur]
                cur = nex
            else:
                break

    def _dis(self, pair) -> int:
        """Return the square of Euclidean distance"""
        return pair[0]**2 + pair[1]**2


class Solution:
    """
    Approach 3: Quick Select
    time: average: O(n), worst: O(n^2), best: O(n)
    space: average: O(logn), worst: O(n), best: O(logn)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        self._quick_select(points, 0, len(points)-1, k)
        return points[:k]

    def _partition(self, arr, low, high):
        """Return the pivot index after partition."""
        pivot = arr[low]  # choose arr[low] as the pivot
        left = low
        for right in range(low+1, high+1):
            if self._dis(arr[right]) < self._dis(pivot):
                arr[left+1], arr[right] = arr[right], arr[left+1]
                left += 1
        arr[low], arr[left] = arr[left], arr[low]
        return left

    def _random_partition(self, arr, low, high):
        """Randomly choose pivot by swapping."""
        pivot_idx = random.randint(low, high)  # Random choose pivot
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
        return self._partition(arr, low, high)

    def _quick_select(self, arr, low, high, k):
        """Sort the array by Divide and Conquer."""
        if low >= high:
            return
        # mid = self._partition(arr, low, high)  # nonrandom
        mid = self._random_partition(arr, low, high)   # random
        if mid < k-1:
            self._quick_select(arr, mid+1, high, k)
        elif mid > k-1:
            self._quick_select(arr, low, mid-1, k)

    def _dis(self, pair) -> int:
        """Return the square of Euclidean distance"""
        return pair[0]**2 + pair[1]**2
