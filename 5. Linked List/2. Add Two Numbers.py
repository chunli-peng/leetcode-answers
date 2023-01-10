# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 1: Simulation
    time: O(max(m,n)), space: O(1)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1+n2+carry

            carry = 1 if total > 9 else 0  # slow: total//10
            cur.next  = ListNode(total-10 if total > 9 else total)  # slow: total%10

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
