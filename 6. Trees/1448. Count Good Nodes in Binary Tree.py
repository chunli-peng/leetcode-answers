# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: BFS
    time: O(n), space: O(n)
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return
        res = 0
        queue = [[root, root.val]]  # pair: [node, max_val]
        while queue:
            node, max_val = queue.pop(0)
            if node.val >= max_val:
                res += 1
                max_val = node.val
            if node.left:
                queue.append([node.left, max_val])
            if node.right:
                queue.append([node.right, max_val])
        return res


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return
        res = 0
        stack = [[root, root.val]]  # pair: [node, max_val]
        while stack:
            node, max_val = stack.pop(0)
            if node.val >= max_val:
                res += 1
                max_val = node.val
            if node.right:
                stack.append([node.right, max_val])
            if node.left:
                stack.append([node.left, max_val])
        return res


class Solution:
    """
    Approach 3: Recursive DFS
    time: O(n), space: O(n)
    """
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node=root, max_val=root.val):
            if not node:
                return
            if node.val >= max_val:
                self.res += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs()
        return self.res
