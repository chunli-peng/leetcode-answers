class BrowserHistory:
    """
    Approach 1: Doubly Linked List
    time: O(1) for visit(), O(steps) for back() and forward()
    space: O(n) for Linked List
    """
    def __init__(self, homepage: str):
        self.cur = DLinkedNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = DLinkedNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps != 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps != 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


class DLinkedNode:
    def __init__(self, value=None, prev=None, next=None):
        self.val, self.prev, self.next = value, prev, next


class BrowserHistory:
    """
    Approach 2: Dynamic Array
    time: O(1) for all functions
    space: O(n) for Linked List
    """
    def __init__(self, homepage: str):
        self.i, self.length = 0, 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.i += 1
        if self.i > len(self.history) - 1:  # not: self.i > self.length-1
            self.history.append(url)
        else:
            self.history[self.i] = url
        self.length = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.length - 1)
        return self.history[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
