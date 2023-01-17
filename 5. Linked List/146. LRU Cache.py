class LRUCache:
    """
    Approach 1: Hash Table + Doubly Linked List
    time: O(1), space: O(capacity)
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.head, self.tail = DlinkedNode(), DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = DlinkedNode(key, value)
        self.add_to_head(self.cache[key])

        if len(self.cache) > self.capacity:
            removed = self.tail.prev
            self.remove_node(removed)
            del self.cache[removed.key]

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class DlinkedNode:
    def __init__(self, key=None, value=None):
        self.key, self.val = key, value
        self.prev = self.next = None


class LRUCache:
    """
    Approach 1.2: Ordered Dictionary (Built-in package)
    time: O(1), space: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.odic = OrderedDict()

    def get(self, key: int) -> int:
        value = self.odic.get(key)
        if not value:
            self.odic.move_to_end(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.odic[key] = value
        self.odic.move_to_end(key)
        if len(self.odic) > self.capacity:
            self.odic.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
