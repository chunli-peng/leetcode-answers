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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h_left = self.maxDepth(root.left)
        h_right = self.maxDepth(root.right)
        return max(h_right, h_left)+1


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, 1]]  # pair: [node, depth]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        return res


class Solution:
    """
    Approach 2.2: Iterative DFS (alternative code)
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        stack = [[root, 1]]  # pair: [node, depth]
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res


class Solution:
    """
    Approach 3.2: BFS (alternative code)
    time: O(n), space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        queue = [[root, 1]]  # pair: [node, depth]
        while queue:
            node, depth = queue.pop()
            res = max(res, depth)
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        return res
