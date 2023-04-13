class Solution:
    """
    Approach 1: Quick Sort (Partition-exchange Sort) (Unaccepted)
    detail: Exceeded time limit, traditional quick sort cannot pass the case with many duplicates.
    time: average: O(nlogn), worst: O(n^2), best: O(nlogn)
    space: average: O(logn), worst: O(n), best: O(logn) for function stack
    Requirement: time: O(nlogn)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums)-1)
        return nums

    def _partition(self, arr, low, high):
        """Return the pivot index after partition."""
        pivot = arr[low]  # choose arr[low] as the pivot
        left = low
        for right in range(low+1, high+1):
            if arr[right] < pivot:
                arr[left+1], arr[right] = arr[right], arr[left+1]
                left += 1
        arr[low], arr[left] = arr[left], arr[low]
        return left

    def _random_partition(self, arr, low, high):
        """Randomly choose pivot by swapping."""
        pivot_idx = random.randint(low, high)  # Random choose pivot
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
        return self._partition(arr, low, high)

    def _quick_sort(self, arr, low, high):
        """Sort the array by Divide and Conquer."""
        if low >= high:
            return
        # mid = self._partition(arr, low, high)  # nonrandom
        mid = self._random_partition(arr, low, high)   # random
        self._quick_sort(arr, low, mid-1)
        self._quick_sort(arr, mid+1, high)


class Solution:
    """
    Approach 1.2: Three-way Quick Sort (Partition-exchange Sort)
    detail: Compared to the traditional quicksort, which partitions the array \
        into two parts based on a pivot element, three-way quicksort partitions
        the array into three parts: elements < pivot, elements
        = pivot, and elements > the pivot.
    time: average: O(nlogn), worst: O(n^2), best: O(nlogn)
    space: average: O(logn), worst: O(n), best: O(logn)
    Requirement: time: O(nlogn)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quick_sort_3(nums, 0, len(nums)-1)
        return nums

    def _partition_3(self, arr, low, high):
        """Return pivot indice after Three-way partition."""
        pivot = arr[low]  # choose arr[low] as the pivot
        left, i, right = low, low+1, high+1
        while i < right:
            if arr[i] > pivot:
                arr[i], arr[right-1] = arr[right-1], arr[i]
                right -= 1
            elif arr[i] < pivot:
                arr[left+1], arr[i] = arr[i], arr[left+1]
                i += 1
                left += 1
            else:
                i += 1
        arr[low], arr[left] = arr[low], arr[left]
        return left, right

    def _random_partition(self, arr, low, high):
        """Randomly choose pivot by swapping."""
        pivot_idx = random.randint(low, high)  # Random choose pivot index
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
        return self._partition_3(arr, low, high)

    def _quick_sort_3(self, arr, low, high):
        """Sort the array by Divide and Conquer."""
        if low >= high:
            return
        mid_left, mid_right = self._random_partition(arr, low, high)
        self._quick_sort_3(arr, low, mid_left)
        self._quick_sort_3(arr, mid_right, high)


class Solution:
    """
    Approach 2: Heap Sort
    time: O(nlogn), space: O(1)
    Requirement: time: O(nlogn)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        self._heap_sort(nums)
        return nums

    def _heap_sort(self, nums):
        n = len(nums)
        self._max_heapify(nums, 0, n)
        for i in range(n-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self._max_heappop(nums, 0, i)

    def _max_heapify(self, heap, root, heap_len):
        """Build a max heap."""
        for i in range(heap_len-1, -1, root-1):
            self._max_heappop(heap, i, len(heap))

    def _max_heappop(self, heap, root, heap_len):
        """Pop the maximum to the top of heap"""
        cur = root
        while cur*2+1 < heap_len:
            left, right = cur*2+1, cur*2+2
            if heap_len <= right or heap[left] > heap[right]:
                nex = left
            else:
                nex = right
            if heap[cur] < heap[nex]:
                heap[cur], heap[nex] = heap[nex], heap[cur]
                cur = nex
            else:
                break


class Solution:
    """
    Approach 3: Merge Sort
    time: T(n) = 2*T(n/2) + 2n, where T is the time complexity of problem.
        According to the Master Theorem, T(n) = O(nlogn)
    space: O(n) for <sorted>, O(logn) for function stack,
        totally, O(nlogn)
    Requirement: time: O(nlogn)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        self._merge_sort(nums, 0, len(nums)-1)
        return nums

    def _merge_sort(self, nums, left, right):
        if left == right:
            return
        mid = (left + right) // 2
        self._merge_sort(nums, left, mid)
        self._merge_sort(nums, mid+1, right)
        sorted = []
        i, j = left, mid+1
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[j] < nums[i]):
                sorted.append(nums[j])
                j += 1
            else:
                sorted.append(nums[i])
                i += 1
        nums[left: right+1] = sorted
