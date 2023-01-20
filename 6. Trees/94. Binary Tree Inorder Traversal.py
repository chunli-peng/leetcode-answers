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
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res


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
        res, predecessor = [], None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res
