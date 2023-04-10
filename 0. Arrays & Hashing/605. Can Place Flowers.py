class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        dp = [0] + flowerbed + [0]
        for i in range(1, len(dp)-1):
            if dp[i] == 0 and dp[i-1] == 0 and dp[i+1] == 0:
                dp[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        prev, curr = 0, 0
        for i in range(length):
            prev, curr = curr, flowerbed[i]
            if ((i == 0 or prev == 0)  # previous element
               and (curr == 0)  # current element
               and (i == length-1 or flowerbed[i+1] == 0)):  # next element
                curr = 1
                n -= 1
            if n <= 0:
                return True
        return False


class Solution:
    """
    Approach 2: Greedy
    time: O(n), space: O(1)
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = abs(flowerbed[0]-1)

        for bed in flowerbed:
            if bed:
                n -= int((empty-1) / 2)  # int division, round toward zero
                empty = 0
                if n <= 0:  # pruning
                    return True
            else:
                empty += 1

        n -= (empty) // 2
        return n <= 0
