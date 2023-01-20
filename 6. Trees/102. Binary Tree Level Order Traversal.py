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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


class Solution:
    """
    Approach 1.2: BFS (alternative code)
    time: O(n), space: O(n)
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [[root, 1]]  # pair: [node, depth]
        while queue:
            node, depth = queue.pop(0)
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        return res


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [[root, 1]]  # pair: [node, depth]
        while stack:
            node, depth = stack.pop()
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            if node.right:
                stack.append([node.right, depth+1])
            if node.left:
                stack.append([node.left, depth+1])
        return res


class Solution:
    """
    Approach 3: Recursive DFS
    time:  O(n), space: O(n)
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(node=root, depth=1):
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        dfs()
        return res
