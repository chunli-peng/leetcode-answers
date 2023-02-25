class Solution:
    """
    Approach 1: Recursive DFS + Array
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph>, O(n) for <visited>
        totally O(m+n).
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses  # 0: unvisited, 1: unfinished, 2: finished

        for course, req in prerequisites:
            graph[req].append(course)

        def dfs(i) -> bool:
            if visited[i] > 0:
                return visited[i] == 2
            visited[i] = 1
            for j in graph[i]:
                if not dfs(j):  # find a circle
                    return False
            visited[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    """
    Approach 1.2: Recursive DFS + Hash Table
    time: O(m+n), where m is the edge number, m is the vertex number.
    space: O(m+n) for the <graph>, O(n) for hash table <finished>,
        O(n) for function stack, totally, O(m+n).
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        finished = {}  # None: unvisited, True: unfinished, False: finished

        for course, req in prerequisites:
            graph[req].append(course)

        def dfs(i) -> bool:
            if i in finished:
                return finished[i]
            finished[i] = False
            for j in graph[i]:
                if not dfs(j):  # find a circle
                    return False
            finished[i] = True
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    """
    Approach 2: Topological Sort + BFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the graph <graph>, O(n) for <queue> <in_deg>
        totally O(m+n).
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            graph[req].append(course)
            in_deg[course] += 1

        queue = [i for i, deg in enumerate(in_deg) if deg == 0]
        while queue:
            i = queue.pop(0)
            for j in graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    queue.append(j)

        res = [i for i, deg in enumerate(in_deg) if deg == 0]
        return len(res) == numCourses


class Solution:
    """
    Approach 3: Topological Sort + Iterative DFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the reverse graph <rev_graph>, O(n) for <stack> <in_deg>
        totally O(m+n).
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            graph[req].append(course)
            in_deg[course] += 1

        stack = [i for i, deg in enumerate(in_deg) if deg == 0]
        while stack:
            i = stack.pop()
            for j in graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    stack.append(j)

        res = [i for i, deg in enumerate(in_deg) if deg == 0]
        return len(res) == numCourses
