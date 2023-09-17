# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS
    time: O(n^2), space: O(n^2) for hash table <seen>
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        res = set()

        def dfs(node):
            if not node:
                return ""
            # detail: serialize a tree by: node(node.left)(node.right)
            serial = "".join([
                str(node.val), "(",
                dfs(node.left), ")(",
                dfs(node.right), ")",
            ])

            if (subtree := seen.get(serial, None)):
                res.add(subtree)
            else:
                seen[serial] = node
            return serial

        dfs(root)
        return list(res)


class Solution:
    """
    Approach 2: Recursive DFS + Triples
    time: O(n), space: O(n) for hash table <seen>
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        res = set()
        idx = 0

        def dfs(node):
            if not node:
                return 0
            triple = (node.val, dfs(node.left), dfs(node.right))
            # detail: serialize a tree by: (node, node.left, node.right)
            #                              (val, index, index)
            if triple in seen:
                (subtree, index) = seen[triple]
                res.add(subtree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[triple] = (node, idx)
                return idx

        dfs(root)
        return list(res)
