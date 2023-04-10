class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n*sqrt(n)), space: O(n)
    """
    def numSquares(self, n: int) -> int:
        dp = [0] + [1] + [0]*(n-1)
        for i in range(2, n+1):
            temp = n  # n times of 1
            for j in range(1, int(i**0.5)+1):
                temp = min(temp, dp[i-j**2])
            dp[i] = 1 + temp
        return dp[-1]


class Solution:
    """
    Approach 2: BFS + Memory Search
    time: O(n*sqrt(n)), space: O(sqrt(n))
    """
    def numSquares(self, n: int) -> int:
        ps = [i*i for i in range(1, int(n**0.5)+1)][::-1]
        p_set = set(ps)
        queue, cache = [n], {n: 1}
        while queue:
            val = queue.pop(0)
            if val in p_set:
                return cache[val]
            for p in ps:
                if val-p > 0 and val-p not in cache:
                    queue.append(val-p)
                    cache[val-p] = cache[val] + 1


class Solution:
    """
    Approach 3: Greedy + Recursive DFS + Math
    time: O(sqrt(n)), space: O(1) for function stack, O(sqrt(n)) for <ps>
    """
    def numSquares(self, n: int) -> int:
        ps = [i*i for i in range(1, int(n**0.5)+1)][::-1]
        p_set = set(ps)

        def dfs(n, count):
            if count == 1:
                return n in p_set
            for p in ps:
                if dfs(n-p, count-1):
                    return True
            return False

        for i in range(1, 5):  # Lagrange's four-square theorem
            if dfs(n, i):
                return i


class Solution:
    """
    Approach 4: Math (Lagrange's four-square theorem)
    time: O(sqrt(n)), space: O(1)
    """
    def numSquares(self, n: int) -> int:
        # Check: n = 4^k*(8m+7)
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        # Check: n = a^2 + b^2
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return bool(a) + bool(b)
            a += 1

        return 3
