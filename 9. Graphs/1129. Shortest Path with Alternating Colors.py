class Solution:
    """
    Approach 1: BFS
    time: O(n+r+b), where r = len(redEdges), b = len(blueEdges),
    space: O(n+r+b) for <red_graph>, <blue_graph>, O(n) for <queue>,
        totally, O(n+r+b).
    """
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = collections.defaultdict(list)
        blue_graph = collections.defaultdict(list)

        for a, b in redEdges:
            red_graph[a].append(b)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        answer = [-1 for _ in range(n)]
        queue = [(0, 0, None)]  # [(node, distance, prev_color), ...]  color: 0-red 1-blue
        visited = set()
        visited.add((0, None))  # {(node, prev_color), ...}

        while queue:
            node, dist, prev_color = queue.pop(0)
            if answer[node] == -1:
                answer[node] = dist

            if prev_color != 0:  # color = blue or None
                for child in blue_graph[node]:
                    if (child, 0) not in visited:
                        queue.append((child, dist+1, 0))
                        visited.add((child, 0))

            if prev_color != 1:  # color = red or None
                for child in red_graph[node]:
                    if (child, 1) not in visited:
                        queue.append((child, dist+1, 1))
                        visited.add((child, 1))

        return answer


class Solution:
    """
    Approach 1.2: BFS (alternative code)
    time: O(n+r+b), where r = len(redEdges), b = len(blueEdges),
    space: O(n+r+b) for <graph>, O(n) for <queue>,
        totally, O(n+r+b).
    """
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for a, b in redEdges:
            graph[a].append((b, 0))  # color: 0-red
        for u, v in blueEdges:
            graph[u].append((v, 1))  # 1-blue

        answer = [-1 for _ in range(n)]
        queue = [(0, 0, None)]  # [(node, distance, prev_color), ...]
        visited = set()
        visited.add((0, None))  # {(node, prev_color), ...}

        while queue:
            node, dist, prev_color = queue.pop(0)
            if answer[node] == -1:
                answer[node] = dist

            for child, color in graph[node]:
                if color != prev_color and (child, color) not in visited:
                    queue.append((child, dist+1, color))
                    visited.add((child, color))

        return answer
