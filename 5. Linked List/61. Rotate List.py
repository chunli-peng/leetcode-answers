# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Stack
    time: O(n), space:(n)
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        stack, length, cur = [], 0, head
        while cur:
            stack.append(cur)
            cur = cur.next
            length += 1
        stack[-1].next = head  # Merge

        k = k % length
        while stack and k:
            stack.pop()
            k -= 1
        new_head = stack[-1].next
        stack[-1].next = None  # Split
        return new_head


class Solution:
    """
    Approach 2: Create Circle
    time: O(n), space:(1)
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        length, cur = 1, head
        while cur.next:
            cur = cur.next
            length += 1

        cur.next = head  # Merge
        for _ in range(length - k % length):
            cur = cur.next
        new_head = cur.next
        cur.next = None  # Split
        return new_head
