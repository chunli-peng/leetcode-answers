class Solution:
    """
    Approach 1: Heap Sort by Min Heap (built-in func)
    time: O(n) for heapify() in Python, space: O(1)
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
    time: O(n) for heapify() in Python, space: O(n)
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
    time: O(nlogn) for heapify, O(klogn) for adjust
        totally, O(nlogn)
    space: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self._max_heapify(nums, n)  # build a max heap

        for j in range(n-1, n-k-1, -1):  # pop k-1 times from heap
            nums[0], nums[j] = nums[j], nums[0]  # storing top element in bottom
            self._max_heap_adjust(nums, 0, j-1)  # rebuild max heap
        return nums[-k]

    def _max_heapify(self, arr: List[int], n: int) -> List[int]:
        """Build max heap, heap is a full binary tree"""
        for i in range(n//2-1, -1, -1):  # build a max heap by bottom up
            self._max_heap_adjust(arr, i, n-1)

    def _max_heap_adjust(self, arr: List[int], top: int, end: int) -> List[int]:
        """Adjust the max heap by Moving the top element down"""
        i = top
        j = 2*i + 1  # <j> is the left leaf of the root <i>
        while j <= end:
            if j+1 <= end and arr[j+1] > arr[j]:  # choose the largest leaf
                j += 1

            if arr[i] < arr[j]:  # if parent is smaller than children
                arr[i], arr[j] = arr[j], arr[i]  # exchange
                i = j  # pointer move down
                j = 2*i + 1
            else:
                break


class Solution:
    """
    unfinished
    Approach 2: QuickSelect
    Time Complexity:
        - Best Case: O(n)
        - Average Case: O(n)
        - Worst Case: O(n^2)
    Extra Space Complexity: O(1)
    Requirement: time: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self._partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break
        return nums[k]

    def _partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        nums[fill], nums[right] = nums[right], nums[fill]
        return fill


class Solution:
    """
    Approach 3: QuickSelect
    Time Complexity:
        - Best Case: O(n)
        - Average Case: O(n)
        - Worst Case: O(n^2)
    Extra Space Complexity: O(1)
    Requirement: time: O(n)
    https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/by-flix-amc8/
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr:List[int], low:int, high:int)-> int:
            pivot = arr[low]
            left, right = low, high
            while left < right:
                while left<right and pivot <= arr[right]:
                    right -= 1
                arr[left] = arr[right]
                while left<right and pivot >= arr[left]:
                    left += 1
                arr[right] = arr[left]
            arr[left] = pivot
            return left

        def randomPartition(arr:List[int], low:int, high:int)-> int:
            pivot_index = random.randint(low,high)
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
            return partition(arr,low,high)

        def topSplit(arr:List[int], low:int, high:int, k:int)-> int:
            mid = randomPartition(arr,low,high)
            if mid == k-1:
                return arr[mid]
            elif mid < k-1:
                return topSplit(arr, mid+1, high, k)
            else:
                return topSplit(arr, low, mid-1, k)

        n = len(nums)
        return topSplit(nums,0,n-1,n-k+1)

