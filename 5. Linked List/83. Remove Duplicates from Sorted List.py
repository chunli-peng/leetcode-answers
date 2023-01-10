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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


class Solution:
    """
    Approach 1.2: Iteration (alternative code)
    time: O(n), space: O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
