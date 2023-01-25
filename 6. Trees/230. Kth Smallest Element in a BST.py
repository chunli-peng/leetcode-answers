# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS (Inorder Traversal)
    time: O(n), space: O(n)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root=root):
            return inorder(root.left) + [root.val] + \
                inorder(root.right) if root else []
        return inorder()[k - 1]


class Solution:
    """
    Approach 2: Iterative DFS (Inorder Traversal)
    time: O(H+k), where H is the height of the tree, best: O(logn+k), worst: O(n+k)
    space: O(H), best: O(logn), worst: O(n)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


class Solution:
    """
    Approach 3: DFS + Dictionary
    time: O(n) for pretreatment, O(H) for searching, where H is the height of the tree, \
        best: O(logn), worst: O(n)
    space: O(n) for storing the tree
    Follow-up requirement: If you need to find the kth smallest frequently, how would you optimize?
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        bst = MyBst(root)
        return bst.kth_smallest(k)


class MyBst:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self._node_num = {}
        self._count_node_num(root)

    def kth_smallest(self, k: int):
        """Return the k-th smallest value"""
        node = self.root
        while node:
            left = self._node_num[node.left] if node.left else 0
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _count_node_num(self, node) -> int:
        """Count the numbers of children according to root"""
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]


class Solution:
    """
    Approach 4: AVL tree (Adelson-Velsky and Landis, self-balancing binary search tree)
    time: O(n) for pretreatment, O(H) for inseart, delete, and search, where H is the height of the tree.
    space: O(n) for storing the tree
    Follow-up requirement: If the BST is modified often (i.e., we can do insert and delete operations) \
        and you need to find the kth smallest frequently, how would you optimize?
    https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solutions/1050055/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07/
    """
