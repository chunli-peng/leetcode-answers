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
    Approach 2: BFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue_1, queue_2 = [p], [q]
        while queue_1 and queue_2:
            node_1, node_2 = queue_1.pop(0), queue_2.pop(0)
            if node_1.val != node_2.val:
                return False
            left_1, right_1 = node_1.left, node_1.right
            left_2, right_2 = node_2.left, node_2.right
            if (not left_1) ^ (not left_2):
                return False
            if (not right_1) ^ (not right_2):
                return False
            if left_1:
                queue_1.append(left_1)
                queue_2.append(left_2)
            if right_1:
                queue_1.append(right_1)
                queue_2.append(right_2)
        return True
