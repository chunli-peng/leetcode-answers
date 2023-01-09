# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Approach 1: Hash Set
    time: O(m+n), space: O(m), where m is the length of headA
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None


class Solution:
    """
    Approach 2: Two Pointers
    time: O(m+n), space: O(1)
    Follow-up requirement: time: O(m+n), space: O(1)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_A, p_B = headA, headB
        while p_A != p_B:
            # if there is no intersection, p_A = p_B = None
            p_A = p_A.next if p_A else headB
            p_B = p_B.next if p_B else headA
        return p_A
