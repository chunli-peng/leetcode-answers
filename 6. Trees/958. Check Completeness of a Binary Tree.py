# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: BFS
    time: O(n), space: O(n)
    """
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            else:
                while queue:
                    node = queue.pop(0)
                    if node:
                        return False
        return True


class Solution:
    """
    Approach 2: BFS + Indexing
    time: O(n), space: O(n)
    """
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 1)]
        num = 0

        while queue:
            node, idx = queue.pop(0)
            num += 1
            if node.left:
                queue.append((node.left, 2*idx))
            if node.right:
                queue.append((node.right, 2*idx+1))

        return idx == num



class Solution:
    """
    Approach 2.2: BFS + Indexing + Pruning
    time: O(n), space: O(n)
    """
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 1)]
        num = 0

        while queue:
            node, idx = queue.pop(0)
            num += 1
            if idx > num:  # Pruning
                return False

            if node.left:
                queue.append((node.left, 2*idx))
            if node.right:
                queue.append((node.right, 2*idx+1))

        return True
