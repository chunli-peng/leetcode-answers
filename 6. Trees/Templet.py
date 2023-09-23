"""
Code Example from Problem 104:
"""

class Solution:
    """
    Approach 1: Recursive DFS
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h_left = self.maxDepth(root.left)
        h_right = self.maxDepth(root.right)
        return max(h_right, h_left) + 1


class Solution:
    """
    Approach 2.2: Iterative DFS
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        stack = [(root, 1)]  # [(node, depth), ...]
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))
        return res


class Solution:
    """
    Approach 3: BFS
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        queue = [root]
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res


class Solution:
    """
    Approach 3.2: BFS (alternative code)
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        queue = [(root, 1)]  # [(node, level), ...]
        while queue:
            node, level = queue.pop(0)
            res = max(res, level)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return res
