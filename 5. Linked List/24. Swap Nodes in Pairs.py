# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Recursion
    time: O(n), space: O(n)
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(1)
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr and curr.next:
            nxt_pair = curr.next.next
            next = curr.next

            # reverse the pair
            next.next = curr
            curr.next = nxt_pair
            prev.next = next

            prev = curr
            curr = nxt_pair
        return dummy.next
