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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res, self.prev_depth = None, 0

        def dfs(node=root, depth=1):
            if not node:
                return
            if self.prev_depth < depth:
                self.res = node.val
                self.prev_depth = depth
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs()
        return self.res


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        res, prev_depth = None, 0
        stack = [[root, 1]]  # pair: [node, depth]
        while stack:
            node, depth = stack.pop()
            if prev_depth < depth:
                res = node.val
                prev_depth = depth
            if node.right:
                stack.append([node.right, depth+1])
            if node.left:
                stack.append([node.left, depth+1])
        return res


class Solution:
    """
    Approach 3: BFS
    time: O(n), space: O(n)
    """
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            res = node.val
        return res


class Solution:
    """
    Approach 3.2: BFS (alternative code)
    time: O(n), space: O(n)
    """
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        prev_depth = 0
        queue = [[root, 1]]  # pair: [node, depth]
        while queue:
            node, depth = queue.pop(0)
            if prev_depth < depth:
                res = node.val
                prev_depth = depth
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        return res
