class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(mn), where m=len(coins), n=amount
    space: O(n)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float(inf)] * amount
        for i in coins:
            for j in range(i, amount+1):
                dp[j] = min(dp[j], dp[j-i]+1)
        return dp[amount] if dp[amount] != float(inf) else -1


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(mn), where m=len(coins), n=amount
    space: O(n) for <queue> and <visited>
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = [(amount, 0)]
        visited = set()
        while queue:
            rest, n = queue.pop(0)
            if rest == 0:
                return n
            for coin in coins:
                if rest >= coin and rest-coin not in visited:
                    queue.append((rest-coin, n+1))
                    visited.add(rest-coin)
        return -1


class Solution:
    """
    Approach 3: Recursive DFS + Memory Search
    time: O(mn), where m=len(coins), n=amount
    space: O(n) for <cache> and function stack
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount=amount):
            if amount in cache:
                return cache[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            res = int(10**4+1)
            for coin in coins:
                n = dfs(amount-coin)
                if n >= 0 and n+1 < res:
                    res = n + 1
            cache[amount] = res if res < int(10**4+1) else -1
            return cache[amount]
        return dfs()


class Solution:
    """
    Approach 3.2: Recursive DFS + Memory Search (Built-in Func)
    time: O(mn), where m=len(coins), n=amount
    space: O(n) for cache and function stack
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amount=amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            res = int(10**4+1)
            for coin in coins:
                n = dfs(amount-coin)
                if n >= 0 and n+1 < res:
                    res = n + 1
            return res if res < int(10**4+1) else -1
        return dfs()
