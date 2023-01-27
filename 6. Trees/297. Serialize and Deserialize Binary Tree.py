# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Approach 1: Recursive DFS (Preorder Traversal)
    time: O(n), space: O(n)
    """
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        res = []

        def dfs(node=root):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs()
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        vals = data.split(",")
        self.index = 0

        def dfs():
            if vals[self.index] == "#":
                self.index += 1
                return
            root = TreeNode(int(vals[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()


class Codec:
    """
    Approach 1.2: Recursive DFS (Preorder Traversal) (alternative code)
    time: O(n), space: O(n)
    """
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return '#'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' \
            + str(self.serialize(root.right))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        def dfs(queue):
            val = queue.pop(0)
            if val == "#":
                return
            return TreeNode(int(val), dfs(queue), dfs(queue))
        return dfs(data.split(","))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
