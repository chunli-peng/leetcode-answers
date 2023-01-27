# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion
    time: O(2^n), more details in wiki Catalan number.
    space: O(2^n)
    """
    def __init__(self) -> None:
        self.cache = {
            0: [],
            1: [TreeNode(0)],
        }  # list of FBT

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:  # all numbers of FBT are even
            return []

        if n not in self.cache:
            res = []
            for left_num in range(n):
                for left_tree in self.allPossibleFBT(left_num):
                    for right_tree in self.allPossibleFBT(n-1-left_num):
                        root = TreeNode(0, left_tree, right_tree)
                        res.append(root)
            self.cache[n] = res
        return self.cache[n]
