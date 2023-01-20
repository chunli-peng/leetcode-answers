# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS (Inorder Traversal)
    time:  O(n), space: O(logn)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return
        # default: root at right point of mid
        # n -= 1  # root at left point of mid
        left = self.sortedArrayToBST(nums[:n//2])
        mid = nums[n//2]
        right = self.sortedArrayToBST(nums[n//2+1:])
        return TreeNode(mid, left, right)
