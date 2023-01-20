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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(root1.val+root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val+root2.val)
        stack = [[merged, root1, root2]]
        while stack:
            node, node_1, node_2 = stack.pop()
            left_1, right_1 = node_1.left, node_1.right
            left_2, right_2 = node_2.left, node_2.right

            if right_1 and right_2:
                node.right = TreeNode(right_1.val+right_2.val)
                stack.append([node.right, right_1, right_2])
            elif right_1:
                node.right = right_1
            elif right_2:
                node.right = right_2

            if left_1 and left_2:
                node.left = TreeNode(left_1.val+left_2.val)
                stack.append([node.left, left_1, left_2])
            elif left_1:
                node.left = left_1
            elif left_2:
                node.left = left_2

        return merged


class Solution:
    """
    Approach 3: BFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val+root2.val)
        queue = [[merged, root1, root2]]
        while queue:
            node, node_1, node_2 = queue.pop(0)
            left_1, right_1 = node_1.left, node_1.right
            left_2, right_2 = node_2.left, node_2.right

            if left_1 and left_2:
                node.left = TreeNode(left_1.val+left_2.val)
                queue.append([node.left, left_1, left_2])
            elif left_1:
                node.left = left_1
            elif left_2:
                node.left = left_2

            if right_1 and right_2:
                node.right = TreeNode(right_1.val+right_2.val)
                queue.append([node.right, right_1, right_2])
            elif right_1:
                node.right = right_1
            elif right_2:
                node.right = right_2

        return merged
