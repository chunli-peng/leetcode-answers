class MyLinkedList:
    """
    Approach 1: Singly Linked List
    time: O(index) for get(), addAtIndex(), O(1) for addAtHead(), O(n) for addAtTail()
    space: O(n) for Linked List
    """
    def __init__(self):
        self.size = 0
        self.head = LinkedNode()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self._get_prev_node(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        prev = self._get_prev_node(index)
        prev.next = LinkedNode(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self._get_prev_node(index)
        prev.next = prev.next.next
        self.size -= 1

    def _get_prev_node(self, index: int) -> 'LinkedNode':
        """Get the node at (index-1) """
        prev = self.head
        for _ in range(index):
            prev = prev.next
        return prev


class LinkedNode:
    def __init__(self, value=None, next=None):
        self.val, self.next = value, next


class MyLinkedList:
    """
    Approach 2: Doubly Linked List
    time: O(index) for get(), addAtIndex(), O(1) for addAtHead(), O(n) for addAtTail()
    space: O(n) for Linked List
    """
    def __init__(self):
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self._get_prev_node(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        prev = self._get_prev_node(index)
        succ = prev.next
        new_node = DLinkedNode(val, prev, succ)
        prev.next, new_node.next.prev = new_node, new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self._get_prev_node(index)
        succ = prev.next.next
        prev.next, succ.prev = succ, prev
        self.size -= 1

    def _get_prev_node(self, index: int) -> 'DLinkedNode':
        """Get the node at (index-1) """
        if index <= self.size // 2:
            prev = self.head
            for _ in range(index):
                prev = prev.next
        else:
            prev = self.tail
            for _ in range(self.size - index + 1):
                prev = prev.prev
        return prev


class DLinkedNode:
    def __init__(self, value=None, prev=None, next=None):
        self.val, self.prev, self.next = value, prev, next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
