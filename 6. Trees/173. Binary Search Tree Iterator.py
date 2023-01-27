# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    """
    Approach 1: Serialization + Recursive DFS (Inorder Traversal)
    time: O(n) for pretreatment, O(1) for next() and hasNext()
    space: O(n) for storing
    """
    def __init__(self, root: Optional[TreeNode]):
        self.cur = -1
        self.vals = self._inorder(root)  # Serialization

    def next(self) -> int:
        self.cur = self.cur + 1
        return self.vals[self.cur]

    def hasNext(self) -> bool:
        if self.cur != len(self.vals)-1:
            return True
        return False

    def _inorder(self, root: Optional[TreeNode]) -> List:
        """Return the list of inorder traversal"""
        if not root:
            return []
        return self._inorder(root.left) + [root.val] + \
            self._inorder(root.right)


class BSTIterator:
    """
    Approach 2: Iterative DFS (Inorder Traversal)
    time: average O(1) for next() with n times, O(1) for hasNext()
    space: O(h) for the stack, worst: O(n)
    Follow-up requirement: average O(1) time and O(h) space for next() and hasNext()
    """
    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        if self.hasNext:  # not necessary, since next() always be valid.
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.stack.pop()
            res = self.cur.val
            self.cur = self.cur.right
            return res

    def hasNext(self) -> bool:
        if self.cur or self.stack:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
