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


class Codec:
    """
    Approach 2: BFS
    time: O(n), space: O(n)
    """
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return []
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != '#':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
