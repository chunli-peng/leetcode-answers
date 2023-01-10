# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Approach 1: hash Table
    time: O(n), space: O(n)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


class Solution:
    """
    Approach 2: Slow-fast Pointers (Floyd's cycle-finding algorithm)
    time: O(n), space: O(1)
    Follow-up requirement: space: O(1)
    """
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
