class Solution:
    """
    Approach 1: Recursive DFS
    time: O(m+n), where m is the edge number, n is the vertex number,
        O(n) for m=n.
    space: O(n) for the call stack, O(n) for <graph>.
    """
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # create a undirected graph
        graph = collections.defaultdict(list)
        for par, chi in roads:
            graph[par].append(chi)
            graph[chi].append(par)

        res = 0

        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in graph[node]:
                if child != parent:
                    num = dfs(child, node)
                    passengers += num
                    res += int(ceil(num / seats))
            return passengers + 1

        dfs(0, -1)
        return res
