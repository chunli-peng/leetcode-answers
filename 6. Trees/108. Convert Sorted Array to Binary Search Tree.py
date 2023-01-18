# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Inorder Traversal (right point of mid)
    time:  O(n), space: O(logn)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return
        left = self.sortedArrayToBST(nums[:n//2])
        mid = nums[n//2]
        right = self.sortedArrayToBST(nums[n//2+1:])
        return TreeNode(mid, left, right)


class Solution:
    """
    Approach 1.2: Inorder Traversal (left point of mid)
    time:  O(n), space: O(logn)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return
        n -= 1
        left = self.sortedArrayToBST(nums[:n//2])
        mid = nums[n//2]
        right = self.sortedArrayToBST(nums[n//2+1:])
        return TreeNode(mid, left, right)
