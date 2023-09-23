"""
Note: This question is the same as 530
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS (Inorder Traversal)
    time: O(n), space: O(1)
    """
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node=root):
            if not node:
                return

            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return res


class Solution:
    """
    Approach 2: Iterative DFS (Inorder Traversal)
    time: O(n), space: O(1)
    """
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float('inf')

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev:
                res = min(res, root.val - prev.val)
            prev = root
            root = root.right
        return res
