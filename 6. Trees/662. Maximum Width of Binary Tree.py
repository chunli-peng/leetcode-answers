# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: BFS + Indexing
    time: O(n), space: O(n)
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1

        queue = [(root, 1)]  # [(node, index), ...]
        while queue:
            length = len(queue)
            level = []

            for _ in range(length):
                node, idx = queue.pop(0)
                level.append(idx)
                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx+1))
            res = max(res, max(level)-min(level)+1)
        return res


class Solution:
    """
    Approach 1.2: BFS + Indexing (alternative code)
    time: O(n), space: O(n)
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        prev_level, leftmost = 0, 1

        queue = [(root, 1, 0)]  # [(node, index, level), ...]
        while queue:
            node, idx, level = queue.pop(0)
            if level > prev_level:
                prev_level = level
                leftmost = idx
            res = max(res, idx-leftmost+1)
            if node.left:
                queue.append((node.left, 2*idx, level+1))
            if node.right:
                queue.append((node.right, 2*idx+1, level+1))
        return res


class Solution:
    """
    Approach 2: Recursive DFS + Indexing
    time: O(n), space: O(n)
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftmost = {}  # {depth: leftmost index}

        def dfs(node: Optional[TreeNode], depth: int, index: int) -> int:
            if not node:
                return 0
            if depth not in leftmost:
                leftmost[depth] = index
            return max(index - leftmost[depth] + 1,
                       dfs(node.left, depth + 1, index * 2),
                       dfs(node.right, depth + 1, index * 2 + 1))
        return dfs(root, 1, 1)


class Solution:
    """
    Approach 3: Iterative DFS + Indexing
    time: O(n), space: O(n)
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        leftmost = {0: 1}  # {depth: leftmost index}

        stack = [(root, 1, 0)]  # [(node, index, depth), ...]
        while stack:
            node, idx, depth = stack.pop()
            if depth not in leftmost:
                leftmost[depth] = idx
            res = max(res, idx-leftmost[depth]+1)
            if node.right:
                stack.append((node.right, 2*idx+1, depth+1))
            if node.left:
                stack.append((node.left, 2*idx, depth+1))
        return res
