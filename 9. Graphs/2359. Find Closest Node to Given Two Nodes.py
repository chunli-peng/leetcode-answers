class Solution:
    """
    Approach 1: BFS
    time: O(m+n), where m is the edge number, n is the vertex number.
    space: O(m+n) for the <graph>, O(n) for <queue> <dist_1> <dist_2>
        totally O(m+n).
    """
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # create a directed graph
        graph = collections.defaultdict(list)
        for par, chi in enumerate(edges):
            graph[par].append(chi)

        # define a bfs function
        def bfs(root, dist_map):
            """calculate distances between nodes and <root>"""
            queue = [(root, 0)]
            dist_map[root] = 0

            while queue:
                node, dist = queue.pop(0)

                for child in graph[node]:
                    if child not in dist_map:
                        queue.append((child, dist+1))
                        dist_map[child] = dist+1

        dist_1 = {}  # {node: distance between node1 and node}
        dist_2 = {}  # {node: distance between node2 and node}
        bfs(node1, dist_1)
        bfs(node2, dist_2)

        # find a closest node
        res = -1
        res_dist = float("inf")
        for node in range(len(edges)):
            if node in dist_1 and node in dist_2:
                now_dist = max(dist_1[node], dist_2[node])
                if now_dist < res_dist:
                    res, res_dist = node, now_dist

        return res
