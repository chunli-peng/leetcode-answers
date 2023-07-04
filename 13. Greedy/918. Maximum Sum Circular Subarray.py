class Solution:
    """
    Approach 1: Prefix Sum + Monotonic Queue
    time: O(n), space: O(n)
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        # Compute prefix[j] = sum(arr[:j]) for the fixed array arr = nums+nums
        prefix = [0]
        for _ in range(2):
            for num in nums:
                prefix.append(prefix[-1] + num)

        # Want largest prefix[j]-prefix[i] with 1 <= j-i <= n
        # For each j, want smallest prefix[i] with i >= j-n
        res = nums[0]
        queue = collections.deque([0])
        for j in range(1, len(prefix)):
            # If the smallest i is too small, remove it.
            if queue[0] < j-n:
                queue.popleft()

            # The optimal i is queue[0], for cand. answer prefix[j] - prefix[i].
            res = max(res, prefix[j]-prefix[queue[0]])

            # Remove any i1's with prefix[i2] <= prefix[i1].
            while queue and prefix[queue[-1]] >= prefix[j]:
                queue.pop()

            queue.append(j)

        return res


class Solution:
    """
    Approach 2: Kadane's algorithm (Dynamic Programming + Greedy)
    time: O(n), space: O(1)
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0

        for num in nums:
            total += num
            cur_max = max(cur_max+num, num)
            cur_min = min(cur_min+num, num)
            glob_max = max(cur_max, glob_max)
            glob_min = min(cur_min, glob_min)

        return max(glob_max, total-glob_min) if glob_max > 0 else glob_max
