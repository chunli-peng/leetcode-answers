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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [[root, root.val]]  # pair: [node, cur_sum]
        while stack:
            node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == targetSum:
                return True
            if node.right:
                stack.append([node.right, cur_sum+node.right.val])
            if node.left:
                stack.append([node.left, cur_sum+node.left.val])
        return False


class Solution:
    """
    Approach 3: BFS
    time: O(n), space: O(n)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = [[root, root.val]]  # pair: [node, cur_sum]
        while queue:
            node, cur_sum = queue.pop(0)
            if not node.left and not node.right and cur_sum == targetSum:
                return True
            if node.left:
                queue.append([node.left, cur_sum+node.left.val])
            if node.right:
                queue.append([node.right, cur_sum+node.right.val])
        return False
