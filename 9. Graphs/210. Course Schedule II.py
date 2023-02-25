class Solution:
    """
    Approach 1: Recursive DFS + Array
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph>, O(n) for <queue> <visited>
        totally O(m+n).
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses  # 0: unvisited, 1: unfinished, 2: finished
        res = []

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
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]


class Solution:
    """
    Approach 1.2: Recursive DFS + Hash Table
    time: O(m+n), where m is the edge number, m is the vertex number.
    space: O(m+n) for the <graph>, O(n) for hash table <finished>,
        O(n) for function stack, totally, O(m+n).
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        finished = {}  # None: unvisited, True: unfinished, False: finished
        res = []

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
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]


class Solution:
    """
    Approach 2: Topological Sort + BFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph>, O(n) for <queue> <in_deg>
        totally O(m+n).
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            graph[req].append(course)
            in_deg[course] += 1

        res = []
        queue = [i for i, deg in enumerate(in_deg) if deg == 0]
        while queue:
            i = queue.pop(0)
            res.append(i)
            for j in graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    queue.append(j)

        return res if len(res) == numCourses else []


class Solution:
    """
    Approach 3: Topological Sort + Iterative DFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for <graph>, O(n) for <stack> <in_deg>
        totally O(m+n).
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0 for _ in range(numCourses)]

        for course, req in prerequisites:
            graph[req].append(course)
            in_deg[course] += 1

        res = []
        stack = [i for i, deg in enumerate(in_deg) if deg == 0]
        while stack:
            i = stack.pop()
            res.append(i)
            for j in graph[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    stack.append(j)

        return res if len(res) == numCourses else []
