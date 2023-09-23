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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])  # index of root in the inorder list
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(n)
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return

        root = TreeNode(postorder[-1])
        stack = [root]
        idx_inoder = -1

        for i in range(-2, -1-len(postorder), -1):
            child_val = postorder[i]
            node = stack[-1]
            if node.val != inorder[idx_inoder]:
                # construct right subtree at first
                node.right = TreeNode(child_val)
                stack.append(node.right)
            else:
                # construct left subtree
                while stack and stack[-1].val == inorder[idx_inoder]:
                    node = stack.pop()
                    idx_inoder -= 1
                node.left = TreeNode(child_val)
                stack.append(node.left)
        return root
