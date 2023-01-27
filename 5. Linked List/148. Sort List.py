# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Top Down Merge Sort
    time: O(nlogn), space: O(logn)
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        right = self.sortList(mid.next)
        mid.next = None  # Split
        left = self.sortList(head)
        return self.merge_lists(left, right)

    def get_mid(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge_lists(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        while head_1 and head_2:
            if head_1.val > head_2.val:
                prev.next = head_2
                head_2 = head_2.next
            else:
                prev.next = head_1
                head_1 = head_1.next
            prev = prev.next
        prev.next = head_1 if head_1 else head_2
        return dummy.next


class Solution:
    """
    Approach 2: Bottom Up Merge Sort
    time: O(nlogn), space: O(1)
    Follow-up requirements: time: O(nlogn), space: O(1)
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        total_len = self.get_len(head)
        sub_len = 1
        while sub_len < total_len:
            prev, curr = dummy, dummy.next
            while curr:
                head_1 = curr
                curr = self.get_next_head_and_split(curr, sub_len)
                head_2 = curr
                curr = self.get_next_head_and_split(curr, sub_len)
                prev.next = self.merge_lists(head_1, head_2)
                while prev.next:
                    prev = prev.next
            sub_len <<= 1   # same to subLen *= 2
        return dummy.next

    def get_len(self, head: ListNode) -> int:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        return length

    def get_next_head_and_split(self, curr: ListNode, sub_len: int) -> ListNode:
        for _ in range(1, sub_len):
            if curr and curr.next:
                curr = curr.next
            else:
                break
        if curr:  # Split
            temp = curr.next
            curr.next = None
            curr = temp
        return curr

    def merge_lists(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        while head_1 and head_2:
            if head_1.val > head_2.val:
                prev.next = head_2
                head_2 = head_2.next
            else:
                prev.next = head_1
                head_1 = head_1.next
            prev = prev.next
        prev.next = head_1 if head_1 else head_2
        return dummy.next
