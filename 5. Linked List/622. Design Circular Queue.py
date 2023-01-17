class MyCircularQueue:
    """
    Approach 1: Linked List
    time: O(1), space: O(k)
    """
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.tail = ListNode(None)
        self.head = ListNode(None, self.tail)
        self.tail.next = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


class MyCircularQueue:
    """
    Approach 2: Array
    time: O(1), space: O(k)
    """
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.length = k+1
        self.items = [0] * self.length

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items[self.rear] = value
        self.rear = (self.rear+1) % self.length
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front+1) % self.length
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.items[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.items[(self.rear-1) % self.length]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear+1) % self.length == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
