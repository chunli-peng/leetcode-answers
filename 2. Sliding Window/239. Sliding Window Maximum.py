class Solution:
    """
    Approach 1: Priority Queue + Max Heap
    time: O(nlogn), space: O(n)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # default heap is min heap
        queue = [(-nums[i], i) for i in range(k)]
        heapq.heapify(queue)
        res = [-queue[0][0]]
        for i in range(k, n):
            heapq.heappush(queue, (-nums[i], i))
            while queue[0][1] <= i-k:
                # don't need remove all elements that not in heap immediately:
                heapq.heappop(queue)
            res.append(-queue[0][0])
        return res


class Solution:
    """
    Approach 2: Monotonic Queue
    time: O(n), space: O(k)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        n = len(nums)
        res = []

        for right in range(n):
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            while queue[0] <= right-k:  # left = i-k
                queue.popleft()
            if right >= k-1:
                res.append(nums[queue[0]])
        return res


class Solution:
    """
    Approach 3: Partitioning + Sliding Window
    time: O(n), space: O(n)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_max, suffix_max = [0]*n, [0]*n
        for i in range(n):
            if i % k == 0:
                prefix_max[i] = nums[i]
            else:
                prefix_max[i] = max(prefix_max[i-1], nums[i])
        for i in range(n-1, -1, -1):
            if i == n-1 or (i+1) % k == 0:
                suffix_max[i] = nums[i]
            else:
                suffix_max[i] = max(suffix_max[i+1], nums[i])
        res = [max(suffix_max[i], prefix_max[i+k-1]) for i in range(n-k+1)]
        return res
