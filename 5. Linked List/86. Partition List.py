# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Simulation
    time: O(n), space: O(1)
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_left, dummy_right = ListNode(), ListNode()
        left, right = dummy_left, dummy_right

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        left.next = dummy_right.next  # merge
        right.next = None
        return dummy_left.next
