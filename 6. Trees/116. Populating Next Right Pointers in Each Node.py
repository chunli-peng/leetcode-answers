"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    """
    Approach 1: BFS
    time: O(n), space: O(n)
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i != n-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution:
    """
    Approach 2: Using Next Pointers
    time: O(n), space: O(1)
    Follow-up requirement: space: O(1)
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root


class Solution:
    """
    Approach 3: Recursion (DFS)
    time: O(n), space: O(1), You may assume implicit stack space does not count as extra space for this problem.
    Follow-up requirement: space: O(1), The recursive approach is fine.
    """
    def connect(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        while left:
            left.next = right
            left = left.right
            right = right.left
        self.connect(root.left)
        self.connect(root.right)
        return root


class Solution:
    """
    Approach 3.2: Recursion (DFS)
    time: O(n), space: O(1), You may assume implicit stack space does not count as extra space for this problem.
    Follow-up requirement: space: O(1), The recursive approach is fine.
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        def dfs(node_1=root.left, node_2=root.right):
            if not node_1:
                return
            node_1.next = node_2
            dfs(node_1.left, node_1.right)
            dfs(node_2.left, node_2.right)
            dfs(node_1.right, node_2.left)

        dfs()
        return root
