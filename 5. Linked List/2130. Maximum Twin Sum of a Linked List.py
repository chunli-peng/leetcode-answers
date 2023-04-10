# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Reverse List + Fast-slow Pointers
    time: O(n), space: O(1)
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse the first half part
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        # calculate twin sums
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return res
