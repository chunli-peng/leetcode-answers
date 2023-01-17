# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Insertion Sort
    time: O(n^2), space: O(1)
    """
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            curr.next, prev.next, curr = prev.next, curr, curr.next

        return dummy.next
