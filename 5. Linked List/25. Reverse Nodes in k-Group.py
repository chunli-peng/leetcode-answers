# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Imitation
    time: O(n), space: O(1)
    Follow-up requirement: space: O(1)
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        while True:
            tail = self.get_kth(prev, k)
            if not tail:
                return dummy.next
            next_group = tail.next
            head, tail = self.reverse(head, tail)
            prev.next, tail.next = head, next_group
            prev, head = tail, tail.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, head, tail):
        prev, curr = None, head
        while prev != tail:
            curr.next, prev, curr = prev, curr, curr.next
        return tail, head
