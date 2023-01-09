# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 1: Approach 1: Copy into Array List + Two Pointers
    time: O(n), space: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


class Solution:
    """
    Approach 2: Recursion
    time: O(n), space: O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head

        def check(right=head):
            if right:
                if not check(right.next):
                    return False
                if self.left.val != right.val:
                    return False
                self.left = self.left.next
            return True
        return check()


class Solution:
    """
    Approach 3: Fast-slow Pointers
    time: O(n), space: O(1)
    Follow-up requirements: time: O(n), space: O(1)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        cur = None
        slow = head
        fast = head

        # reverse the front half linked list
        while fast and fast.next:
            fast = fast.next.next
            cur, slow.next, slow = slow, cur, slow.next

        if fast:  # even
            slow = slow.next  # move back since reversion
        while slow:  # check palindrome
            if slow.val != cur.val:
                return False
            slow = slow.next
            cur = cur.next
        return True
