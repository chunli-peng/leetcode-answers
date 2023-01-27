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
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_gain(node=root):
            """the max gain of the root is the max sum of path \
                from the root to the leaf"""
            if not node:
                return 0

            left_gain = max_gain(node.left)
            right_gain = max_gain(node.right)
            self.res = max(self.res, node.val+left_gain+right_gain)
            temp = node.val + max(left_gain, right_gain)
            return temp if temp > 0 else 0
        max_gain()
        return self.res
