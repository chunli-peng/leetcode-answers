# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack = [[p, q]]
        while stack:
            node_1, node_2 = stack.pop()
            if node_1.val != node_2.val:
                return False
            if (not node_1.left) ^ (not node_2.left):
                return False
            if (not node_1.right) ^ (not node_2.right):
                return False
            if node_1.right:
                stack.append([node_1.right, node_2.right])
            if node_1.left:
                stack.append([node_1.left, node_2.left])
        return True


class Solution:
    """
    Approach 3: BFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue = [[p, q]]
        while queue:
            node_1, node_2 = queue.pop(0)
            if node_1.val != node_2.val:
                return False
            if (not node_1.left) ^ (not node_2.left):
                return False
            if (not node_1.right) ^ (not node_2.right):
                return False
            if node_1.left:
                queue.append([node_1.left, node_2.left])
            if node_1.right:
                queue.append([node_1.right, node_2.right])
        return True
