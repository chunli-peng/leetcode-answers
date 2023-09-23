# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion + Memory Search
    time: O(G_n) for all trees with O(n) nodes, where G_n is Catalan Number, G_n = O(4^n / n^0.5),
        totally, O(n*G_n)
    space: O(n) for recursion stack, O(G_n) for <cache> with O(n) nodes,
        totally, O(n*G_n)
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}  # [(start, end): TreeNode]

        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in cache:
                return cache[(start, end)]

            res = []
            for mid in range(start, end+1):
                for left in generate(start, mid-1):
                    for right in generate(mid+1, end):
                        root = TreeNode(mid, left, right)
                        res.append(root)
            cache[(start, end)] = res
            return res

        return generate(1, n)
