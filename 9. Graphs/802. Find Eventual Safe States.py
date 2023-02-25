class Solution:
    """
    Approach 1: Recursive DFS + Array
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(n) for <visited>, O(n) for function stack,
        totally O(n).
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n  # 0: unvisited, 1: unfinished, 2: finished

        def dfs(i) -> bool:
            if visited[i] > 0:
                return visited[i] == 2
            visited[i] = 1
            for j in graph[i]:
                if not dfs(j):  # find a circle
                    return False
            visited[i] = 2
            return True

        return [i for i in range(n) if dfs(i)]


class Solution:
    """
    Approach 1.2: Recursive DFS + Hash Table
    time: O(m+n), where m is the edge number, m is the vertex number.
    space: O(n) for hash table <safe>, O(n) for function stack,
        totally O(n).
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}  # None: unvisited, True: unfinished, False: finished

        def dfs(i) -> bool:
            if i in safe:
                return safe[i]
            safe[i] = False
            for j in graph[i]:
                if not dfs(j):  # find a circle
                    return False
            safe[i] = True
            return True

        return [i for i in range(n) if dfs(i)]


class Solution:
    """
    Approach 2: Topological Sort + BFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the reverse graph <rev_graph>, O(n) for <queue> <in_deg>
        totally O(m+n).
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rev_graph[y].append(x)
        in_deg = [len(ys) for ys in graph]

        queue = [i for i, deg in enumerate(in_deg) if deg == 0]  # safe vertex
        while queue:
            i = queue.pop(0)
            for j in rev_graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    queue.append(j)

        return [i for i, deg in enumerate(in_deg) if deg == 0]  # safe vertex


class Solution:
    """
    Approach 3: Topological Sort + Iterative DFS
    time: O(m+n), where m is the edge number, m is the vertex number.
    space: O(m+n) for the reverse graph <rev_graph>, O(n) for <stack> <in_deg>
        totally O(m+n).
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rev_graph[y].append(x)
        in_deg = [len(ys) for ys in graph]

        stack = [i for i, deg in enumerate(in_deg) if deg == 0]  # safe vertex
        while stack:
            i = stack.pop()
            for j in rev_graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    stack.append(j)

        return [i for i, deg in enumerate(in_deg) if deg == 0]  # safe vertex
