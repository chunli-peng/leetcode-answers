# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS
    time: O(n), space: O(n) for function stack
    Follow-up requirement: Could you solve it both recursively and iteratively?
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return (
                left.val == right.val and
                dfs(left.left, right.right) and
                dfs(left.right, right.left)
            )
        return dfs(root.left, root.right)


class Solution:
    """
    Approach 2: Interative DFS
    time: O(n), space: O(n)
    Follow-up requirement: Could you solve it both recursively and iteratively?
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        return True


class Solution:
    """
    Approach 2: BFS
    time: O(n), space: O(n)
    Follow-up requirement: Could you solve it both recursively and iteratively?
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
