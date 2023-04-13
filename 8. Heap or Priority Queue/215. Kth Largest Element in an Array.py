class Solution:
    """
    Approach 1: Heap Sort by Min Heap (built-in func)
    time: O(n) for heapify() in Python, O(klogn) for heappop()
        totally, O(n+klogn), which < O(nlogn)
    space: O(1)
    Requirement: time: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)  # min heap
        for _ in range(n-k+1):
            res = heapq.heappop(nums)
        return res


class Solution:
    """
    Approach 1.2: Heap Sort by Max heap (built-in func)
    time: O(n) for heapify() in Python, O(klogn) for heappop()
    space: O(1)
    Requirement: time: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for _ in range(k):
            res = heapq.heappop(max_heap)
        return -res


class Solution:
    """
    Approach 1.3: Heap Sort (user-builted func)
    time:  O(klogk) for building a heap, O((n-k)logk) for pushing,
        totally, O(nlogk)
    space: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # build the min heap with size of k
        self._min_heapify(nums, 0, k)

        # push the remains to the heap
        for i in range(k, n):
            if nums[i] > nums[0]:
                nums[i], nums[0] = nums[0], nums[i]
                self._min_heappop(nums, 0, k)
        return nums[0]

    def _min_heapify(self, heap, root, heap_len):
        """Build a min heap."""
        for i in range(heap_len-1, -1, root-1):
            self._min_heappop(heap, i, heap_len)

    def _min_heappop(self, heap, root, heap_len):
        """Pop the minimum to the top of heap."""
        cur = root
        while cur*2+1 < heap_len:
            left, right = cur*2+1, cur*2+2
            if heap_len <= right or heap[left] < heap[right]:
                nex = left
            else:
                nex = right
            if heap[cur] > heap[nex]:
                heap[cur], heap[nex] = heap[nex], heap[cur]
                cur = nex
            else:
                break


class Solution:
    """
    Approach 2: Quick Select
    time: average: O(n), worst: O(n^2), best: O(n)
    space: average: O(logn), worst: O(n), best: O(logn)
    Requirement: time: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self._quick_select(nums, 0, len(nums)-1, k)
        return nums[k-1]

    def _partition(self, arr, low, high):
        """Return the pivot index after partition."""
        pivot = arr[low]  # choose arr[low] as the pivot
        left = low
        for right in range(low+1, high+1):
            if arr[right] > pivot:
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
