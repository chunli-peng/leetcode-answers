class MinStack:
    """
    Approach 1: Two Stacks
    time: O(1), space: O(n)
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


class MinStack:
    """
    Approach 2: One Stack
    time: O(1), space: O(n)
    detail: Keep differences in the stack.
    """
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            top_val = self.min_val
            self.min_val = top_val - diff
        else:
            top_val = self.min_val + diff
        return top_val

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            top_val = self.min_val
        else:
            top_val = self.min_val + diff
        return top_val

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
