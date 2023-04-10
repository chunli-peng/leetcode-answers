# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: One Pointer
    time: O(n), space: O(1)
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        k, cur = 0, head
        while k < n // 2:
            k += 1
            cur = cur.next
        return cur


class Solution:
    """
    Approach 2: Fast-slow Pointers
    time: O(n), space: O(1)
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow