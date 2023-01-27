# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS + dynamic Programming
    time:  O(n), space: O(n)
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node=root):
            if not node:
                return 0, 0
            left_child_steal, left_child_not = dfs(node.left)
            right_child_steal, right_child_not = dfs(node.right)
            steal = node.val + left_child_not + right_child_not
            not_steal = max(left_child_not, left_child_steal) + \
                max(right_child_not, right_child_steal)
            return steal, not_steal
        return max(dfs())
