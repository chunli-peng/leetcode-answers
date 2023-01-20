class Solution:
    """
    Approach 1: Recursive DFS
    time: O(n), space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        if not left_node:
            return right_node
        if not right_node:
            return left_node
        return root


class Solution:
    """
    Approach 2: Recursive DFS + Hash Table
    time: O(n), space: O(n)
    detail: Save ancestors in the hash table.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root: None}

        def dfs(node=root):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs()
        p1, p2 = p, q
        while p1 != p2:
            p1 = dic.get(p1, q)
            p2 = dic.get(p2, p)
        return p1
