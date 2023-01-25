# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS
    time: O(n), space: O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node=root, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and \
                dfs(node.right, node.val, upper)
        return dfs()


class Solution:
    """
    Approach 2: Iterative DFS (Inorder Traversal)
    time: O(n), space: O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder, stack = float('-inf'), []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
