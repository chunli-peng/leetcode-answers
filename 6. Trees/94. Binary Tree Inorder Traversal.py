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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + \
            self.inorderTraversal(root.right)


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    Follow-up requirement: Iteration
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, cur = [], [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


class Solution:
    """
    Approach 3: Morris Inorder Traversal
    time: O(n), space: O(1)
    Follow-up requirement: Iteration
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:  # If left subtree exists
                prede = self._get_predecessor(root)
                if not prede.right:  # 1st visit
                    prede.right = root  # Connect predecessor and root for backing
                    root = root.left
                else:  # 2nd visit
                    res.append(root.val)
                    prede.right = None  # Disconnect predecessor and root
                    root = root.right  # Visit the right subtree
            else:  # If left subtree does not exist
                res.append(root.val)
                root = root.right  # back and start the 2nd visit
        return res

    def _get_predecessor(self, root):
        """Get the predecessor of the root, if the left tree exists"""
        prede = root.left  # Visit the left subtree
        while prede.right and prede.right != root:
            prede = prede.right
        return prede
