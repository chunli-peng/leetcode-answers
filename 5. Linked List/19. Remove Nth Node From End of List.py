# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 1: Calculate list length
    time: O(n), space: O(1)
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(next=head)
        cur = dummy
        for _ in range(length-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


class Solution:
    """
    Approach 2: Stack
    time: O(n), space: O(n)
    Follow-up requirement: One Pass
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        stack = []
        curr = dummy
        while curr:
            stack.append(curr)
            curr = curr.next

        for _ in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next


class Solution:
    """
    Approach 3: Two Pointers
    time: O(n), space: O(1)
    Follow-up requirement: One Pass
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        left = dummy
        right = head
        for _ in range(n):
            right = right.next

        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return dummy.next
