# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Approach 1: Two Pass Iteration
    time: O(n), space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q = self.get_path(root, p), self.get_path(root, q)
        ancester = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancester = u
            else:
                break
        return ancester

    def get_path(self, root: TreeNode, target: TreeNode) -> List[TreeNode]:
        node, path = root, []
        while node != target:
            path.append(node)
            if node.val < target.val:
                node = node.right
            else:
                node = node.left
        path.append(node)
        return path


class Solution:
    """
    Approach 2: One Pass Iteration
    time: O(n), space: O(1)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                return ancestor


class Solution:
    """
    Approach 3: One Pass Recursion
    time: O(n), space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        if p.val < ancestor.val and q.val < ancestor.val:
            return self.lowestCommonAncestor(ancestor.left, p, q)
        elif p.val > ancestor.val and q.val > ancestor.val:
            return self.lowestCommonAncestor(ancestor.right, p, q)
        else:
            return ancestor


class Solution:
    """
    Approach 4: Recursive DFS
    time: O(n), space: O(n)
    related: Same to the problem: 236. Lowest Common Ancestor of a Binary Tree
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
    Approach 5: Recursive DFS + Hash Table
    time: O(n), space: O(n)
    detail: Save ancestors in the hash table.
    related: Same to the problem: 236. Lowest Common Ancestor of a Binary Tree
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
