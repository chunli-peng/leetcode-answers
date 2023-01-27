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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root=root, perv_sum=0) -> int:
            if not root:
                return 0
            curr_sum = perv_sum*10 + root.val
            if not root.left and not root.right:
                return curr_sum
            else:
                return dfs(root.left, curr_sum) + dfs(root.right, curr_sum)
        return dfs()


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [[root, 0]]  # pair: [node, prev_sum]
        while stack:
            node, prev_sum = stack.pop()
            curr_sum = prev_sum*10 + node.val
            if not node.left and not node.right:
                res += curr_sum
            if node.right:
                stack.append([node.right, curr_sum])
            if node.left:
                stack.append([node.left, curr_sum])
        return res


class Solution:
    """
    Approach 3: BFS
    time: O(n), space: O(n)
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        queue = [[root, 0]]  # pair: [node, prev_sum]
        while queue:
            node, prev_sum = queue.pop(0)
            curr_sum = prev_sum*10 + node.val
            if not node.left and not node.right:
                res += curr_sum
            if node.left:
                queue.append([node.left, curr_sum])
            if node.right:
                queue.append([node.right, curr_sum])
        return res
