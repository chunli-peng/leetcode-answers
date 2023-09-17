class Solution:
    """
    Approach 1: Recursive DFS + Graph Construction
    time: O(n), space: O(n)
    """
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)

        def dfs(cur, par):
            res = 0

            for child in adj[cur]:
                if child == par:
                    continue
                child_res = dfs(child, cur)
                if child_res or hasApple[child]:
                    res += child_res + 2
            return res

        return dfs(0, -1)
