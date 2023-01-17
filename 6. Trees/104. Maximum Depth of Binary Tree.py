# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion (DFS)
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h_left = self.maxDepth(root.left)
        h_right = self.maxDepth(root.right)
        return max(h_right, h_left)+1


class Solution:
    """
    Approach 2: Iteration (DFS)
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res


class Solution:
    """
    Approach 3: BFS
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        if root:
            queue.append(root)
        res = 0

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res
