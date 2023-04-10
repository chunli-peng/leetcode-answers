class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def climbStairs(self, n: int) -> int:
        dp = [1] + [1] + [0] * (n-1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Solution:
    """
    Approach 1.2: Dynamic Programming (Rolling Array)
    time: O(n), space: O(1)
    """
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return curr


class Solution:
    """
    Approach 2: DFS + Memory Search
    time: O(n), space: O(n)
    """
    def __init__(self) -> None:
        self.cache = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]


class Solution:
    """
    Approach 2.2: DFS + Memory Search (Built-in Func)
    time: O(n), space: O(n)
    """
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    """
    Approach 3: Matrix Fast Power
    time: O(logn), space: O(1)
    detail: holonomic sequence: f(n) = f(n-1) + f(n-2)
    """
    def climbStairs(self, n: int) -> int:
        q = [[1, 1], [1, 0]]
        res = self._pow(q, n)
        return res[0][0]

    def _pow(self, q, n):
        res = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                res = self._multiply(res, q)
            n //= 2
            q = self._multiply(q, q)
        return res

    def _multiply(self, a, b):
        m, n, k = len(a), len(b[0]), len(a[0])
        res = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = sum(a[i][x]*b[x][j] for x in range(k))
        return res


class Solution:
    """
    Approach 4: General Term Formula (Math)
    time: O(1), space: O(1)
    """
    def climbStairs(self, n: int) -> int:
        sqrt_5 = math.sqrt(5)
        res = 1/sqrt_5*(
            ((1+sqrt_5)/2)**n - ((1-sqrt_5)/2)**n
            )
        return res
