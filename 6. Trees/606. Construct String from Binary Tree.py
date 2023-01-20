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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return f'{root.val}({self.tree2str(root.left)})'
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'


class Solution:
    """
    Approach 2: Iterative DFS
    time: O(n), space: O(n)
    """
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res, stack, visited = '', [root], set()
        while stack:
            node = stack[-1]
            if node not in visited:
                visited.add(node)
                res += f'({node.val}'
                if not node.left and node.right:
                    res += '()'
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                res += ')'
                stack.pop()
        return res[1:-1]
