# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Same to 1038. Binary Search Tree to Greater Sum Tree
"""

class Solution:
    """
    Approach 1: Recursive DFS (Inorder Traversal)
    time: O(n), space: O(n) for function stack
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node=root):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS (Inorder Traversal) (alternative code)
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
        res, stack = [], []
        cur = root
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
        curr = root
        while curr:
            if curr.left:  # If left subtree exists
                prede = self._get_predecessor(curr)
                if not prede.right:  # 1st visit
                    prede.right = curr  # Connect predecessor and curr for backing
                    curr = curr.left
                else:  # 2nd visit
                    res.append(curr.val)
                    prede.right = None  # Disconnect predecessor and curr
                    curr = curr.right  # Visit the right subtree
            else:  # If left subtree does not exist
                res.append(curr.val)
                curr = curr.right  # Back and start the 2nd visit
        return res

    def _get_predecessor(self, curr):
        """Get the predecessor of the <curr>, if the left tree exists"""
        prede = curr.left  # Visit the left subtree
        while prede.right and prede.right != curr:
            prede = prede.right
        return prede
