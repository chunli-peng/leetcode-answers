class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2*k), space: O(n*k)
    """
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[float('infinity')] * (k + 1) for _ in range(n + 1)]
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        f[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(i, k)+1):  # i >= j
                for x in range(i):
                    val = max(f[x][j-1], prefix_sum[i]-prefix_sum[x])
                    if val <= f[i][j]:
                        f[i][j] = val
                    else:
                        break  # pruning

        return f[n][k]


class Solution:
    """
    Approach 2: Binary Search + Greedy
    time: O(n*log(sum-max)), space: O(1)
    """
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left+right)//2
            if self.check_split(nums, k, mid):
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res

    def check_split(self, nums, k, largest) -> bool:
        cur_sum, num_subarray = 0, 1
        for num in nums:
            cur_sum += num
            if cur_sum > largest:
                num_subarray += 1
                cur_sum = num
        return num_subarray <= k
