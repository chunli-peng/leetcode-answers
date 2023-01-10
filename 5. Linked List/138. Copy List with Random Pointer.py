"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Approach 1: Recursion + Hash Table
    time: O(n), space: O(n)
    """
    def __init__(self) -> None:
        self.hashmap = {None: None}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head in self.hashmap:
            return self.hashmap[head]
        self.hashmap[head] = Node(head.val)
        self.hashmap[head].next = self.copyRandomList(head.next)
        self.hashmap[head].random = self.copyRandomList(head.random)
        return self.hashmap[head]


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(1)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                hashmap[cur].next = hashmap[cur.next]
            if cur.random:
                hashmap[cur].random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]
