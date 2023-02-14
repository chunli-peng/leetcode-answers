# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion
    time: O(n), space: O(n)
    """
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(n)
    """
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root
