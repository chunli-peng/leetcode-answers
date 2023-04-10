class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(n)
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, res = len(nums), 0, 0
        dp = [1]*n  # dp[i] represents the max length from index: 0 -> i
        cnt = [1]*n  # cnt[i] represents the number of max length dp[i]
        for right, num in enumerate(nums):
            for left in range(right):
                if num > nums[left]:
                    if dp[right] < dp[left]+1:  # update
                        dp[right], cnt[right] = dp[left]+1, cnt[left]
                    elif dp[right] == dp[left]+1:
                        cnt[right] += cnt[left]
            if dp[right] > max_len:
                max_len, res = dp[right], cnt[right]
            elif dp[right] == max_len:
                res += cnt[right]
        return res


class Solution:
    """
    Approach 3: Greedy + Prefix Sum + Binary Search
    time: O(nlogn), space: O(n)
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = []  # dp[i][j] represents the ending nums[j] of LIS with length = i
        cnt = []  # cnt[i][j] represents prefix of counts of LIS subseq of dp[i][j]
        for num in nums:
            i = self.binary_search(len(dp), lambda i: num <= dp[i][-1])
            c = 1
            if i != 0:
                k = self.binary_search(len(dp[i-1]), lambda k: dp[i-1][k] < num)
                c = cnt[i-1][-1] - cnt[i-1][k]  # the counts of ending with dp[i][j]
            if i == len(dp):
                dp.append([num])
                cnt.append([0, c])
            else:
                dp[i].append(num)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

    def binary_search(self, n, f: Callable[[int], bool]):
        left, right = 0, n
        while left < right:
            mid = (left+right)//2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left
