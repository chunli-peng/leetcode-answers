class Solution:
    """
    Approach 1: Floyd-Warshall Algorithm
    time: O(n^3), space: O(n^2)
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * numCourses for _ in range(numCourses)]
        for p, c in prerequisites:
            dp[p][c] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = True
        res = []
        for i, j in queries:
            res.append(dp[i][j])
        return res


class Solution:
    """
    Approach 2: Recursive DFS + Memory Search
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph> <cache>, O(n) for function stack,
        totally, O(m+n).
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for req, crs in prerequisites:
            graph[req].append(crs)

        def dfs(req):
            if req not in cache:
                cache[req] = set()
                for crs in graph[req]:
                    cache[req].update(dfs(crs))  # cache[req] |= dfs(crs)
            cache[req].add(req)
            return cache[req]

        cache = {}  # {prereq: {course, ...}}
        for req in range(numCourses):
            dfs(req)

        return [v in cache[u] for u, v in queries]


class Solution:
    """
    Approach 2.2: Recursive DFS + Memory Search (alternative code)
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph>, O(n) for function stack,
        O(n^2) for the cache, totally, O(n^2).
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.graph = collections.defaultdict(list)
        for req, crs in prerequisites:
            self.graph[req].append(crs)
        return [self.dfs(u, v) for u, v in queries]

    @cache
    def dfs(self, start, end):
        if start == end:
            return True
        return any(self.dfs(nxt, end) for nxt in self.graph[start])


class Solution:
    """
    Approach 3: Topological Sort + BFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the graph <graph>, O(n) for <queue> <in_deg>
        totally O(m+n).
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]
        cache = defaultdict(set)  # {course: {prereq, ...}}

        for req, crs in prerequisites:
            graph[req].append(crs)
            in_deg[crs] += 1

        queue = [i for i, deg in enumerate(in_deg) if deg == 0]
        while queue:
            i = queue.pop(0)
            for j in graph[i]:
                cache[j].add(i)
                cache[j].update(cache[i])
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    queue.append(j)

        return [u in cache[v] for u, v in queries]


class Solution:
    """
    Approach 4: Topological Sort + Iterative DFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the graph <graph>, O(n) for <stack> <in_deg>
        totally O(m+n).
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]
        cache = defaultdict(set)  # {course: {prereq, ...}}

        for req, crs in prerequisites:
            graph[req].append(crs)
            in_deg[crs] += 1

        stack = [i for i, deg in enumerate(in_deg) if deg == 0]
        while stack:
            i = stack.pop()
            for j in graph[i]:
                cache[j].add(i)
                cache[j].update(cache[i])
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    stack.append(j)

        return [u in cache[v] for u, v in queries]
