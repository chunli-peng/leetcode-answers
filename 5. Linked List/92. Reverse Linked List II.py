# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Reverse the Total Sublist and Connect (Tail Insertion)
    time: O(n), space: O(1)
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        # reach the left node of sublsit
        curr = dummy
        for _ in range(left-1):
            curr = curr.next
        tail_1 = curr
        tail_2 = curr.next

        # Reverse the total sublist
        prev, curr = None, tail_2
        for _ in range(right-left+1):
            curr.next, prev, curr = prev, curr, curr.next

        # Merge
        tail_1.next = prev  # head_2 = prev
        tail_2.next = curr  # head_3 = curr
        return dummy.next


class Solution:
    """
    Approach 2: Reverse by Head Insertion
    time: O(n), space: O(1)
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        for _ in range(right-left):
            next = curr.next  # a)
            curr.next, next.next, prev.next = next.next, prev.next, next  # b) c) d)
            # # Details:
            # next = curr.next  # a)
            # curr.next = next.next  # b)
            # next.next = prev.next  # c)
            # prev.next = next  # d)
        return dummy.next
