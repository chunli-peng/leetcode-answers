class Solution:
    """
    Approach 1: Union Find
    time: Since union without by Rank, worst: O(nlogn), average: O(n*α(n)), \
        where α is This inverse Ackermann function, \
        and α<5 for practical input.
    space: O(n) for variable <parent>, <rank> in UnionFind.
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(self, x):
            """Find and Return the parent of the point <x>."""
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(i, j):
            parent[find(i)] = find(j)

        for i, j in edges:
            if find(i) != find(j):
                union(i, j)
            else:
                return [i, j]


class Solution:
    """
    Approach 2: Union Find by Rank
    time: O(n*α(n)), where α is This inverse Ackermann function, \
        and α<5 for practical input.
    space: O(n) for variable <parent>, <rank> in UnionFind.
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(edges)
        for i, j in edges:
            if uf.find(i) != uf.find(j):
                uf.unite(i, j)
            else:
                return [i, j]


class UnionFind:
    def __init__(self, edges):
        n = len(edges)
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        """Find and Return the parent of the point <x>."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        """Unite the point <x> and <y>."""
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            elif self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.parent[root_y] = root_x


class Solution:
    """
    Approach 3: Recursive DFS + Hash Table
    time: O(m+n), where m is the edge number, m is the vertex number.
    space: O(m+n) for the <graph>, O(n) for hash table <visited>,
        O(n) for function stack, totally, O(m+n).
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(i, j):
            """Check (i, j) is a redundant connection."""
            visited.add(i)
            for node in graph[i]:
                if node == j:
                    return True
                if node not in visited:
                    if dfs(node, j):
                        return True
            return False

        for i, j in edges:
            if i not in graph:
                graph[i] = {j}
            else:
                visited = set()
                if dfs(i, j):
                    return [i, j]
                else:
                    graph[i].add(j)

            if j not in graph:
                graph[j] = {i}
            else:
                graph[j].add(i)


class Solution:
    """
    Approach 4: BFS + Hash Table
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the graph <graph>, O(n) for <queue>
        totally O(m+n).
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def bfs(i, j):
            """Check (i, j) is a redundant connection."""
            queue = [i]
            while queue:
                i = queue.pop(0)
                visited.add(i)
                for node in graph[i]:
                    if node == j:
                        return True
                    if node not in visited:
                        queue.append(node)
            return False

        for i, j in edges:
            if i not in graph:
                graph[i] = {j}
            else:
                visited = set()
                if bfs(i, j):
                    return [i, j]
                else:
                    graph[i].add(j)

            if j not in graph:
                graph[j] = {i}
            else:
                graph[j].add(i)


class Solution:
    """
    Approach 5: Iterative DFS + Hash Table
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the graph <graph>, O(n) for <stack>
        totally O(m+n).
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def bfs(i, j):
            """Check (i, j) is a redundant connection."""
            stack = [i]
            while stack:
                i = stack.pop()
                visited.add(i)
                for node in graph[i]:
                    if node == j:
                        return True
                    if node not in visited:
                        stack.append(node)
            return False

        for i, j in edges:
            if i not in graph:
                graph[i] = {j}
            else:
                visited = set()
                if bfs(i, j):
                    return [i, j]
                else:
                    graph[i].add(j)

            if j not in graph:
                graph[j] = {i}
            else:
                graph[j].add(i)
