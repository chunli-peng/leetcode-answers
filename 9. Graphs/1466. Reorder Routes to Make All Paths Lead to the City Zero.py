class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(n),
    space: O(n) for hash table <visited> <neighbors> <edges>, O(n) for function stack,
        totally O(n).
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(prev, next) for prev, next in connections}
        neighbors = {city:[] for city in range(n)}
        visited = set([0])
        res = 0

        for prev, next in connections:
            neighbors[prev].append(next)
            neighbors[next].append(prev)

        def dfs(city=0):
            nonlocal edges, neighbors, visited, res
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    res += 1
                visited.add(neighbor)
                dfs(neighbor)
        dfs()
        return res


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(n),
    space: O(n) for hash table <visited> <neighbors> <edges>, O(n) for <queue>,
        totally O(n).
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(prev, next) for prev, next in connections}
        neighbors = [[] for _ in range(n)]
        visited = set([0])
        res = 0

        for prev, next in connections:
            neighbors[prev].append(next)
            neighbors[next].append(prev)

        queue = [0]
        while queue:
            city = queue.pop(0)
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    res += 1
                visited.add(neighbor)
                queue.append(neighbor)
        return res


class Solution:
    """
    Approach 3: BFS + Array
    time: O(n),
    space: O(n) for <visited> <edges>, O(n) for <queue>,
        totally O(n).
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for _ in range(n)]
        visited = [True] + [False] * (n-1)
        res = 0

        for prev, next in connections:  # prev->next
            edges[prev].append((next, 1))  # positive degree: deg(next)=1
            edges[next].append((prev, 0))  # positive degree: deg(prev)=0

        queue = [0]
        while queue:
            curr = queue.pop(0)
            for node, degree in edges[curr]:
                if not visited[node]:
                    res += degree
                    visited[node] = True
                    queue.append(node)
        return res


class Solution:
    """
    Approach 4: Iterative DFS + Array
    time: O(n),
    space: O(n) for <visited> <edges>, O(n) for <stack>,
        totally O(n).
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for _ in range(n)]
        visited = [True] + [False] * (n-1)
        res = 0

        for prev, next in connections:  # prev->next
            edges[prev].append((next, 1))  # positive degree: deg(next)=1
            edges[next].append((prev, 0))  # positive degree: deg(prev)=0

        stack = [0]
        while stack:
            curr = stack.pop()
            for node, degree in edges[curr]:
                if not visited[node]:
                    res += degree
                    visited[node] = True
                    stack.append(node)
        return res
