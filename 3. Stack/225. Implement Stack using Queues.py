class MyStack:
    """
    Approach 1: Two Queues
    time: O(n) for push(), others are O(1),
    space: O(n)
    """
    def __init__(self):
        self.que_1 = collections.deque()
        self.que_2 = collections.deque()

    def push(self, x: int) -> None:
        self.que_2.append(x)
        while self.que_1:
            self.que_2.append(self.que_1.popleft())
        self.que_1, self.que_2 = self.que_2, self.que_1

    def pop(self) -> int:
        return self.que_1.popleft()

    def top(self) -> int:
        return self.que_1[0]

    def empty(self) -> bool:
        return not self.que_1


class MyStack:
    """
    Approach 2: One Queue
    time: O(n) for push(), others are O(1),
    space: O(n)
    Follow-up requirement: One Queue
    """
    def __init__(self):
        self.que = collections.deque()

    def push(self, x: int) -> None:
        self.que.append(x)
        for _ in range(len(self.que)-1):
            self.que.append(self.pop())

    def pop(self) -> int:
        return self.que.popleft()

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
