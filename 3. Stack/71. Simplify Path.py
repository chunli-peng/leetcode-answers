class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)
