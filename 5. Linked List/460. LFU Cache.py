class LFUCache:
    """
    Approach 1: Hash Table + Doubly Linked List
    time: O(1), space: O(capacity)
    Requirement: The functions get and put must each run in O(1) average time complexity.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.least_freq = 0
        self.val_map = {}  # {key: value}
        self.freq_map = collections.defaultdict(int)  # {key: frequence}
        self.list_map = collections.defaultdict(DlinkedList)  # {key: DlinkedList}

    def _counter(self, key):
        counts = self.freq_map[key]
        self.freq_map[key] += 1
        self.list_map[counts].pop(key)
        self.list_map[counts + 1].push_to_tail(key)

        if counts == self.least_freq and self.list_map[counts].length() == 0:
            self.least_freq += 1

    def get(self, key: int) -> int:
        if key not in self.val_map:
            return -1
        self._counter(key)
        return self.val_map[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.val_map and len(self.val_map) == self.cap:
            deleted = self.list_map[self.least_freq].pop_head()
            self.val_map.pop(deleted)
            self.freq_map.pop(deleted)

        self.val_map[key] = value
        self._counter(key)
        self.least_freq = min(self.least_freq, self.freq_map[key])

class DlinkedNode:
    def __init__(self, key=None, value=None):
        self.key, self.val = key, value
        self.prev, self.next = None, None

class DlinkedList:
    def __init__(self):
        self.cache = {}
        self.head, self.tail = DlinkedNode(), DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def length(self):
        return len(self.cache)

    def push_to_tail(self, value):
        node = DlinkedNode(None, value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.cache[value] = node
        self.tail.prev = node
        node.prev.next = node

    def pop(self, value):
        if value in self.cache:
            node = self.cache[value]
            n_prev, n_next = node.prev, node.next
            n_next.prev = n_prev
            n_prev.next = n_next
            self.cache.pop(value, None)

    def pop_head(self):
        res = self.head.next.val
        self.pop(self.head.next.val)
        return res

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LFUCache:
    """
    unfinished
    Approach 2: Two Hash Tables + Doubly Linked List
    time: O(1), space: O(capacity)
    https://leetcode.cn/problems/lfu-cache/solutions/186348/lfuhuan-cun-by-leetcode-solution/
    Requirement: The functions get and put must each run in O(1) average time complexity.
    """
    def __init__(self, capacity: int):
