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
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node=root):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS (alternative code)
    time: O(n), space: O(n) for function stack
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + \
            self.postorderTraversal(root.right) + [root.val]


class Solution:
    """
    Approach 2: Iterative DFS + Two Stacks
    time: O(n), space: O(n) for <stack>
    Follow-up requirement: Iteration
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        res = []

        while stack:
            cur, vis = stack.pop()
            if cur:
                if vis:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return res


class Solution:
    """
    Approach 2.2: Iterative DFS + One Stack
    time: O(n), space: O(n) for <stack>
    Follow-up requirement: Iteration
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        prev, curr = None, root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.right and curr.right != prev:
                stack.append(curr)
                curr = curr.right
            else:
                res.append(curr.val)
                prev = curr
                curr = None
        return res


class Solution:
    """
    Approach 3: Morris Postorder Traversal
    time: O(n), space: O(1)
    Follow-up requirement: Iteration
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            if curr.left:  # If left subtree exists
                prede = self._get_predecessor(curr)
                if not prede.right:  # 1st visit
                    prede.right = curr  # Connect predecessor and curr for backing
                    curr = curr.left
                else:  # 2nd visit
                    prede.right = None  # Disconnect predecessor and curr
                    res.extend(self._add_path(curr.left))
                    curr = curr.right  # Visit the right subtree
            else:  # If left subtree does not exist
                curr = curr.right  # Back and start the 2nd visit
        res.extend(self._add_path(root))  # Get the right side of the tree
        return res

    def _get_predecessor(self, root):
        """Get the predecessor of the root, if the left tree exists"""
        prede = root.left  # Visit the left subtree
        while prede.right and prede.right != root:
            prede = prede.right
        return prede

    def _add_path(self, node):
        """Get a reverse path from <node> to <prede>"""
        temp = []
        while node:
            temp.append(node.val)
            node = node.right
        return temp[::-1]
