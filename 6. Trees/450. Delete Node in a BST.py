# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion
    time: O(n), space: O(n)
    Follow-up requirement: time: O(height of tree)
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # find the min node from left subtree:
            succ = root.right
            while succ.left:
                succ = succ.left
            # exchange the values:
            root.val = succ.val
            # delete the succ.val:
            root.right = self.deleteNode(root.right, root.val)
        return root


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(1)
    Follow-up requirement: time: O(height of tree)
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr, curr_parent = root, None

        while curr and curr.val != key:
            curr_parent = curr
            curr = curr.left if key < curr.val else curr.right

        # if the key not in the tree:
        if not curr:
            return root

        # if key in the tree, cur.val = key:
        if not curr.left and not curr.right:  # <cur> don't have children
            curr = None
        elif not curr.left:  # <cur> only has right child
            curr = curr.right
        elif not curr.right:  # <cur> only has left child
            curr = curr.left
        else:  # both child exists
            succ, succ_parent = curr.right, curr
            while succ.left:  # find the min node from left subtree for replace the <cur>
                succ_parent = succ
                succ = succ.left
            if succ_parent == curr:  # if curr.right is the min
                succ_parent.right = succ.right  # take out <succ>
            else:
                succ_parent.left = succ.right  # take out <succ>
            # replace the <curr>:
            succ.left, succ.right = curr.left, curr.right
            curr = succ  # （can't change curr.val directly）

        if not curr_parent:  # if key = root.val
            return curr
        else:  # if key != root.val, <curr> has parents
            if curr_parent.left and curr_parent.left.val == key:  # key is the left node of <curr_parent>
                curr_parent.left = curr
            else:
                curr_parent.right = curr
        return root
