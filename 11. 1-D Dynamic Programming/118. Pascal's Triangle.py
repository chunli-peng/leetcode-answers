class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n^2), space: O(1)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * i for i in range(1, numRows + 1)]

        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1

        for i in range(numRows):
            for j in range(i):
                if i != 0 and j != 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


class Solution:
    """
    Approach 1.2: Dynamic Programming (alternative code)
    time: O(n^2), space: O(1)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        all_row = [[1]]
        while len(all_row) < numRows:
            new_row = [a+b for a, b in zip([0]+all_row[-1], all_row[-1]+[0])]
            all_row.append(new_row)
        return all_row
