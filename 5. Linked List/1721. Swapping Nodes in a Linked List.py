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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p, q, cur=head, head, head
        i = 1

        while cur:
            if i < k:
                p = p.next
            if i > k:
                q = q.next
            cur = cur.next
            i += 1
        p.val, q.val = q.val, p.val
        return head
