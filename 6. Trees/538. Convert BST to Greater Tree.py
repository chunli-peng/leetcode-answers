# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS (Reverse Inorder Traversal)
    time: O(n), space: O(n)
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.prev_sum = 0

        def dfs(node=root):
            if node:
                dfs(node.right)
                self.prev_sum += node.val
                node.val = self.prev_sum
                dfs(node.left)
        dfs()
        return root


class Solution:
    """
    Approach 1.2: Recursive DFS (Reverse Inorder Traversal) (alternative code)
    time: O(n), space: O(n)
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node=root, prev_sum=0):
            if not node:
                return prev_sum
            node.val += dfs(node.right, prev_sum)
            return dfs(node.left, node.val)
        dfs()
        return root


class Solution:
    """
    Approach 2: Iterative DFS (Reverse Inorder Traversal)
    time: O(n), space: O(n)
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev_sum, stack, cur = 0, [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur.val += prev_sum
            prev_sum = cur.val
            cur = cur.left
        return root


class Solution:
    """
    Approach 3: Reverse Morris Inorder Traversal
    time: O(n), space: O(1)
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev_sum, node = 0, root
        while node:
            if node.right:  # If right subtree exists
                prede = self._get_predecessor(node)
                if not prede.left:  # 1st visit
                    prede.left = node  # Connect predecessor and root for backing
                    node = node.right
                else:  # 2nd visit
                    prede.left = None  # Disconnect predecessor and root
                    node.val += prev_sum
                    prev_sum = node.val
                    node = node.left  # Visit the left subtree
            else:  # If right subtree does not exist
                node.val += prev_sum
                prev_sum = node.val
                node = node.left  # back and start the 2nd visit
        return root

    def _get_predecessor(self, node):
        """Get the predecessor of the root, if the right tree exists"""
        prede = node.right
        while prede.left and prede.left != node:
            prede = prede.left
        return prede
