class Solution:
    """
    Approach 1: Recursive DFS + Memory Search
    time: O((logn)^2), space: O((logn)^2)
    """
    def minDays(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        def dfs(n):
            if n in cache:
                return cache[n]

            one = 1 + n % 2 + dfs(n//2)
            two = 1 + n % 3 + dfs(n//3)
            cache[n] = min(one, two)
            return cache[n]
        return dfs(n)


class Solution:
    """
    Approach 1.2: Recursive DFS + Memory Search (alternative code)
    time: O((logn)^2), space: O((logn)^2)
    """
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))


class Solution:
    """
    Approach 2: Shortest Path (Dijkstra Algorithm) + Graph + Min Heap
    time: For graph G(V,E), Complexity of Dijkstra with Priority Queue is (V+E)log(E),
        where V are vertices, E are edges, totally, O((logn)^2*log(logn)^2)
    space: O((logn)^2)
    """
    def minDays(self, n: int) -> int:
        queue = [(0, n)]  # pair: (days, rest)
        visited = set()
        while True:
            days, rest = heapq.heappop(queue)
            if rest == 1:
                res = days + 1
                break
            if rest not in visited:
                heapq.heappush(queue, (days + rest % 2 + 1, rest // 2))
                heapq.heappush(queue, (days + rest % 3 + 1, rest // 3))
                visited.add(rest)
        return res


class Solution:
    """
    unfinished
    Approach 3: A*
    time: O((logn)^2*loglogn), space: O((logn)^2)
    https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/solutions/384947/chi-diao-n-ge-ju-zi-de-zui-shao-tian-shu-by-leetco/
    """
    def minDays(self, n: int) -> int: