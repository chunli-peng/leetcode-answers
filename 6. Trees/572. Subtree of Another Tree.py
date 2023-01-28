# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursive DFS
    time:  O(m*n), space: O(m+n)
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        return self._is_same_tree(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)

    def _is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self._is_same_tree(p.left, q.left) and \
                self._is_same_tree(p.right, q.right)


class Solution:
    """
    Approach 2: String Matching (KMP, Knuth-Morris-Pratt algorithm)
    time:  O(m+n), space: O(m+n)
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str, subroot_str = self._serialize(root), self._serialize(subRoot)
        return self._kmp(subroot_str.split(","), root_str.split(","))

    def _serialize(self, root) -> str:
        """Serialize Tree by Preorder"""
        if not root:
            return '#'
        return str(root.val) + ',' + str(self._serialize(root.left)) + ',' \
            + str(self._serialize(root.right))

    def _get_lps_array(self, needle: List) -> List:
        """Get Longest Proper Prefix which is also Suffix (LPS) array.
        Example  : ACABACACD
        LPS Array: 001012320
        """
        m = len(needle)
        lps = [0] * m  # lps[0] will always be 0
        prev, curr = 0, 1
        while curr < m:
            if needle[curr] == needle[prev]:
                prev += 1  # Length of Longest Border Increased
                lps[curr] = prev
                curr += 1
            else:
                if prev == 0:  # Only empty border exist
                    lps[curr] = 0
                    curr += 1
                else:  # Try finding longest border for this curr with reduced prev
                    prev = lps[prev-1]
        return lps

    def _kmp(self, needle: List, haystack: List) -> bool:
        """Knuth-Morris-Pratt algorithm to check if 'needle' is in 'haystack'."""
        m, n = len(needle), len(haystack)
        if m > n:
            return False

        haystack_i, needle_i = 0, 0
        lps = self._get_lps_array(needle)
        while haystack_i < n:
            if needle[needle_i] == haystack[haystack_i]:  # Matched increment both
                needle_i += 1
                haystack_i += 1
                if needle_i == m:  # All characters matched
                    return True
            else:
                if needle_i == 0:  # Zero matched
                    haystack_i += 1
                else:
                    needle_i = lps[needle_i-1]  # Shift left
        return False


class Solution:
    """
    Approach 3: Tree Hash + Recursive DFS
    time:  O(m+n), space: O(m+n)
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.cache = set()  # Set to store hashed value of each node.
        self._tree_hash(root, True)  # Calling and adding hash to List
        return self._tree_hash(subRoot, False) in self.cache

    def _tree_hash(self, root, need_each_node):
        """Double Hash Function, return Hash pair in the root or each node."""
        MOD_1 = 1_000_000_007  # large prime number
        MOD_2 = 2_147_483_647  # large prime number

        if not root:
            return (3, 7)

        left_pair = self._tree_hash(root.left, need_each_node)
        right_pair = self._tree_hash(root.right, need_each_node)

        left_1 = (left_pair[0] << 5) % MOD_1
        right_1 = (right_pair[0] << 1) % MOD_1
        left_2 = (left_pair[1] << 7) % MOD_2
        right_2 = (right_pair[1] << 1) % MOD_2

        root_hash_pair = ((left_1 + right_1 + root.val) % MOD_1,
                          (left_2 + right_2 + root.val) % MOD_2)

        if need_each_node:
            self.cache.add(root_hash_pair)

        return root_hash_pair
