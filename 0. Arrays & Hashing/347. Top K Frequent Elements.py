class Solution:
    """
    Approach 1: Trivial Approach
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = collections.Counter(nums)
        return [item[0] for item in hashtable.most_common(k)]


class Solution:
    """
    Approach 2: Quick Select
    time: average: O(n), worst: O(n^2), best: O(n)
    space: average: O(logn), worst: O(n), best: O(logn);
        O(n) for the list <counts>; totally, O(n)
    Follow-up requirement: time complexity better than O(nlogn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(collections.Counter(nums).items())
        self._quick_select(counts, 0, len(counts)-1, k)
        return [item[0] for item in counts[:k]]

    def _partition(self, arr, low, high):
        """Return the pivot index after partition."""
        pivot = arr[low]  # choose arr[low] as the pivot
        left = low
        for right in range(low+1, high+1):
            if arr[right][1] > pivot[1]:
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


class Solution:
    """
    Approach 3: Heap Sort
    time: O(n) for Counter(), O(klogk) for building a heap, O((n-k)logk) for pushing,
        totally, O(nlogk),
    space: O(n) for the list <counts>
    Follow-up requirement: time complexity better than O(nlogn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(collections.Counter(nums).items())
        n = len(counts)
        # build the min heap with size of k
        self._min_heapify(counts, 0, k)

        # push the remains to the heap
        for i in range(k, n):
            if counts[i][1] > counts[0][1]:
                counts[i], counts[0] = counts[0], counts[i]
                self._min_heappop(counts, 0, k)
        return [item[0] for item in counts[:k]]

    def _min_heapify(self, heap, root, heap_len):
        """Build a min heap."""
        for i in range(heap_len-1, -1, root-1):
            self._min_heappop(heap, i, heap_len)

    def _min_heappop(self, heap, root, heap_len):
        """Pop the minimum to the top of heap."""
        cur = root
        while cur*2+1 < heap_len:
            left, right = cur*2+1, cur*2+2
            if heap_len <= right or heap[left][1] < heap[right][1]:
                nex = left
            else:
                nex = right
            if heap[cur][1] > heap[nex][1]:
                heap[cur], heap[nex] = heap[nex], heap[cur]
                cur = nex
            else:
                break


class Solution:
    """
    Approach 4: Counting Sort
    time: O(n+k), space: O(n)
    Follow-up requirement: time complexity better than O(nlogn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
