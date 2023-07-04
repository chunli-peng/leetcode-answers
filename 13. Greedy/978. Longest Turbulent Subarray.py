class Solution:
    """
    Approach 1: Sliding Window
    time: O(n), space: O(1)
    """
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        res, prev = 1, 'start'
        while right < len(arr):
            if arr[right-1] < arr[right] and prev != '<':
                res = max(res, right-left+1)
                right += 1
                prev = '<'
            elif arr[right-1] > arr[right] and prev != '>':
                res = max(res, right-left+1)
                right += 1
                prev = '>'
            else:
                if arr[right] == arr[right-1]:
                    right += 1
                left = right - 1
                prev = 'start'
        return res


class Solution:
    """
    Approach 2: Dynamic Programming
    time: O(n), space: O(n)
    """
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1, 1] for _ in range(n)]
        dp[0][0] = 1  # arr[i-1] > arr[i]
        dp[0][1] = 1  # arr[i-1] < arr[i]

        for i in range(1, n):
            if arr[i-1] > arr[i]:
                dp[i][0] = dp[i-1][1] + 1
            elif arr[i-1] < arr[i]:
                dp[i][1] = dp[i-1][0] + 1

        return max([max(num[0], num[1]) for num in dp])


class Solution:
    """
    Approach 2.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        n = len(arr)
        dp = [1, 1]  # arr[i-1] > arr[i]; arr[i-1] < arr[i]

        for i in range(1, n):
            if arr[i-1] > arr[i]:
                dp[0] = dp[1] + 1
                dp[1] = 1
            elif arr[i-1] < arr[i]:
                dp[1] = dp[0] + 1
                dp[0] = 1
            else:
                dp = [1, 1]
            res = max(res, dp[0], dp[1])
        return res
