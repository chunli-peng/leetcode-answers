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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node=root):
            if not node:
                return 0
            h_left = dfs(node.left)
            h_right = dfs(node.right)
            if h_left == -1 or h_right == -1 or abs(h_left-h_right) > 1:
                return -1
            else:
                return max(h_left, h_right) + 1
        return dfs() != -1
