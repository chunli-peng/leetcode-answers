# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Brute Force (Sorting)
    time: O(knlog(kn)), space: O(kn), where n is the biggest length of sublist.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.val_list = []
        dummy = cur = ListNode()
        for sublist in lists:
            while sublist:
                self.val_list.append(sublist.val)
                sublist = sublist.next
        for val in sorted(self.val_list):
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next


class Solution:
    """
    Approach 2: Heap Queue (Priority Queue)
    time: O(knlogk), space: O(k)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode()
        queue = []
        # Initialization
        for i in range(len(lists)):
            if lists[i]:
                heappush(queue, (lists[i].val, i))
                lists[i] = lists[i].next
        # Create sorted linkied list
        cur = dummy
        while queue:
            val, idx = heappop(queue)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heappush(queue,(lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


class Solution:
    """
    Approach 3: Divide And Conquer by Iteration
    time: O(knlogk), space: O(1)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = len(lists)
        step = 1
        while step < total:
            for i in range(0, total-step, step * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i+step])
            step *= 2
        return lists[0] if total > 0 else None

    def merge_2_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2
        return dummy.next


class Solution:
    """
    Approach 3.2: Divide And Conquer by Recursion
    time: O(knlogk), space: O(logk)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = len(lists)
        step = 1
        while step < total:
            for i in range(0, total-step, step * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i+step])
            step *= 2
        return lists[0] if total > 0 else None

    def merge_2_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.merge_2_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_2_lists(list1, list2.next)
            return list2
