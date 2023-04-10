"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    Approach 1: Recursive DFS + Hash Table
    time: O(n)
    space: O(n) for hash table <old_to_new>, O(n) for function stack,
        totally O(n).
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node) if node else None


class Solution:
    """
    Approach 2: BFS + Hash Table
    time: O(n)
    space: O(n) for hash table <old_to_new>, O(n) for <queue>,
        totally O(n).
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        old_to_new = {}
        queue = [node]
        old_to_new[node] = Node(node.val)

        while queue:
            old = queue.pop(0)
            for neighbor in old.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[old].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]


class Solution:
    """
    Approach 3: Iterative DFS + Hash Table
    time: O(n)
    space: O(n) for hash table <old_to_new>, O(n) for <queue>,
        totally O(n).
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        old_to_new = {}
        stack = [node]
        old_to_new[node] = Node(node.val)

        while stack:
            old = stack.pop()
            for neighbor in old.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                old_to_new[old].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
