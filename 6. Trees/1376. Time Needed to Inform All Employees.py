class Solution:
    """
    Approach 1: Recursive DFS (Top Down) + Graph Construction
    time: O(n),
    space: O(n) for recursion stack, O(n) for <graph>,
        totally, O(n)
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # create graph
        adj = collections.defaultdict(list)
        for idx, par in enumerate(manager):
            adj[par].append(idx)

        def dfs(node):
            time = 0
            for child in adj[node]:
                time = max(time, dfs(child))
            return informTime[node] + time

        return dfs(headID)


class Solution:
    """
    Approach 2: Recursive DFS (Bottom Up) + Memory Search
    time: O(n),
    space: O(n) for recursion stack, O(n) for <cache>,
        totally, O(n)
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == headID:
                return 0
            return dfs(manager[i]) + informTime[manager[i]]
        return max(dfs(i) for i in range(n))


class Solution:
    """
    Approach 3: BFS + Graph Construction
    time: O(n),
    space: O(n) for <queue>, O(n) for <graph>,
        totally, O(n)
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # create graph
        adj = collections.defaultdict(list)
        for idx, par in enumerate(manager):
            adj[par].append(idx)

        res = 0
        queue = [(headID, 0)]  # [(ID, time), ...]
        while queue:
            i, time = queue.pop(0)
            if not adj[i]:
                res = max(res, time)
            else:
                for child in adj[i]:
                    queue.append((child, time+informTime[i]))
        return res


class Solution:
    """
    Approach 3: Iterative DFS (Top Down) + Graph Construction
    time: O(n),
    space: O(n) for <stack>, O(n) for <graph>,
        totally, O(n)
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # create graph
        adj = collections.defaultdict(list)
        for idx, par in enumerate(manager):
            adj[par].append(idx)

        res = 0
        stack = [(headID, 0)]  # [(ID, time), ...]
        while stack:
            i, time = stack.pop()
            if not adj[i]:
                res = max(res, time)
            else:
                for child in adj[i]:
                    stack.append((child, time+informTime[i]))
        return res
