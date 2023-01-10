# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 1: Iteration
    time: O(n), space: O(1)
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


class Solution:
    """
    Approach 1.2: Iteration (alternative code)
    time: O(n), space: O(1)
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next


class Solution:
    """
    Approach 2: Recursion
    time: O(n), space: O(n)
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
