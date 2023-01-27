class Solution:
    """
    Approach 1: Recursive DFS
    time: O(min(m,n)), space: O(min(m,n))
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return self.flipEquiv(root1.left, root2.left) and \
            self.flipEquiv(root1.right, root2.right) or \
            self.flipEquiv(root1.left, root2.right) and \
            self.flipEquiv(root1.right, root2.left)


class Solution:
    """
    Approach 2: Recursive DFS (Canonical Traversal)
    time: O(m+n), space: O(m+n)
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.list_1, self.list_2 = [], []
        self.dfs(root1, self.list_1)
        self.dfs(root2, self.list_2)
        return self.list_1 == self.list_2

    def dfs(self, node: Optional[TreeNode], vals: List) -> None:
        if node:
            vals.append(node.val)
            L = node.left.val if node.left else -1
            R = node.right.val if node.right else -1
            if L < R:
                self.dfs(node.left, vals)
                self.dfs(node.right, vals)
            else:
                self.dfs(node.right, vals)
                self.dfs(node.left, vals)
            vals.append(None)


class Solution:
    """
    Approach 2.2: Recursive DFS (Canonical Traversal) (alternative code)
    time: O(min(m,n)), space: O(min(m,n))
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield None

        return all(x == y for x, y in itertools.zip_longest(dfs(root1), dfs(root2)))
