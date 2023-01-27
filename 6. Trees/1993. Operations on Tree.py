class LockingTree:
    """
    Approach 1: BFS
    time: O(1) for lock(), unlock(), O(n) for upgrade()
    space: O(n)
    """
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.locked = [None] * n
        self.children = {i: [] for i in range(n)}
        for i in range(1, n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # check ancestors
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]

        # check descendants
        can_upgrade, queue = False, [num]
        while queue:
            cur = queue.pop(0)
            if self.locked[cur]:
                self.locked[cur] = None
                can_upgrade = True
            queue.extend(self.children[cur])

        if can_upgrade:
            self.locked[num] = user
        return can_upgrade


class LockingTree:
    """
    Approach 2: Iterative DFS
    time: O(1) for lock(), unlock(), O(n) for upgrade()
    space: O(n)
    """
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.locked = [None] * n
        self.children = {i: [] for i in range(n)}
        for i in range(n-1, 0, -1):  # reverse for dfs
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # check ancestors
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]

        # check descendants
        can_upgrade, stack = False, [num]
        while stack:
            cur = stack.pop()
            if self.locked[cur]:
                self.locked[cur] = None
                can_upgrade = True
            stack.extend(self.children[cur])

        if can_upgrade:
            self.locked[num] = user
        return can_upgrade

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
