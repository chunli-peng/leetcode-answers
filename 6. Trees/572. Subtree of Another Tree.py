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
        return self.is_same_tree(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and \
                self.is_same_tree(p.right, q.right)


class Solution:
    """
    Approach 2: String Matching (KMP, Knuth-Morris-Pratt algorithm)
    time:  O(m+n), space: O(m+n)
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Function to serialize Tree
        def serialize(node, tree_str):
            if node is None:
                tree_str.append('#')
                return

            tree_str.append("^")
            tree_str.append(str(node.val))
            serialize(node.left, tree_str)
            serialize(node.right, tree_str)

        # Knuth-Morris-Pratt algorithm to check if `needle` is in `haystack`
        def kmp(needle, haystack):
            m = len(needle)
            n = len(haystack)

            if n < m:
                return False

            # longest proper prefix which is also suffix
            lps = [0]*m
            # Length of Longest Border for prefix before it.
            prev = 0
            # Iterating from index-1. lps[0] will always be 0
            i = 1

            while i < m:
                if needle[i] == needle[prev]:
                    # Length of Longest Border Increased
                    prev += 1
                    lps[i] = prev
                    i += 1
                else:
                    # Only empty border exist
                    if prev == 0:
                        lps[i] = 0
                        i += 1
                    # Try finding longest border for this i with reduced prev
                    else:
                        prev = lps[prev-1]

            # Pointer for haystack
            haystack_pointer = 0
            # Pointer for needle.
            # Also indicates number of characters matched in current window.
            needle_pointer = 0

            while haystack_pointer < n:
                if haystack[haystack_pointer] == needle[needle_pointer]:
                    # Matched Increment Both
                    needle_pointer += 1
                    haystack_pointer += 1
                    # All characters matched
                    if needle_pointer == m:
                        return True
                else:
                    if needle_pointer == 0:
                        # Zero Matched
                        haystack_pointer += 1
                    else:
                        # Optimally shift left needle_pointer.
                        # Don't change haystack_pointer
                        needle_pointer = lps[needle_pointer-1]

            return False

        # Serialize given Nodes
        root_list = []
        serialize(root, root_list)
        r = "".join(root_list)

        subroot_list = []
        serialize(subRoot, subroot_list)
        s = "".join(subroot_list)

        # Check if s is in r
        return kmp(s, r)


class Solution:
    """
    Approach 3: Tree Hash
    time:  O(m+n), space: O(m+n)
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        MOD_1 = 1_000_000_007
        MOD_2 = 2_147_483_647

        def hash_subtree_at_node(node, need_to_add):
            if node is None:
                return (3, 7)

            left = hash_subtree_at_node(node.left, need_to_add)
            right = hash_subtree_at_node(node.right, need_to_add)

            left_1 = (left[0] << 5) % MOD_1
            right_1 = (right[0] << 1) % MOD_1
            left_2 = (left[1] << 7) % MOD_2
            right_2 = (right[1] << 1) % MOD_2

            hashpair = ((left_1 + right_1 + node.val) % MOD_1,
                        (left_2 + right_2 + node.val) % MOD_2)

            if need_to_add:
                memo.add(hashpair)

            return hashpair

        # List to store hashed value of each node.
        memo = set()

        # Calling and adding hash to List
        hash_subtree_at_node(root, True)

        # Storing hashed value of subRoot for comparison
        s = hash_subtree_at_node(subRoot, False)

        # Check if hash of subRoot is present in memo
        return s in memo
