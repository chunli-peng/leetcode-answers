# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 1: Linear Table
    time: O(n), space: O(n)
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        table = []
        cur = head
        while cur:
            table.append(cur)
            cur = cur.next

        i, j = 0, len(table)-1
        while i < j:
            table[i].next = table[j]
            i += 1
            if i == j:  # even
                break
            table[j].next = table[i]
            j -= 1
        table[i].next = None


class Solution:
    """
    Approach 2: Find Middle Node + Reverse List + Merge Lists
    time: O(n), space: O(1)
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        mid = self.middle_node(head)
        p1, p2 = head, mid.next
        mid.next = None
        p2 = self.reverse_list(p2)
        self.merge_lists(p1, p2)

    def middle_node(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def merge_lists(self, p1: ListNode, p2: ListNode) -> None:
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next, p2.next = p2, tmp1
            p1, p2 = tmp1, tmp2
