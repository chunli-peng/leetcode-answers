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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node=root):
            if not node:
                return 0
            h_left = dfs(node.left)
            h_right = dfs(node.right)
            self.res = max(self.res, h_left+h_right)
            return max(h_left, h_right) + 1
        dfs()
        return self.res
