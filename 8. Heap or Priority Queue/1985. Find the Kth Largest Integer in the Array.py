class Solution:
    """
    Approach 1: Min Heap + string to int
    time: O(n) for heapify() in Python, O(klogn) for heappop()
        totally, O(n+klogn), which < O(nlogn)
    space: O(n)
    """
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = [-int(num) for num in nums]
        heapq.heapify(max_heap)
        res = None
        for _ in range(k):
            res = heapq.heappop(max_heap)
        return str(-res)


class Solution:
    """
    Approach 2: Compare strings
    time: O(mnlogn), where n=len(nums), m is the max length of string
    space: O(m+logn)
    detail: the type int in some languages cannot allow 100 digits.
    """
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=cmp_to_key(self._cmp))
        return nums[k-1]

    def _cmp(self, n1: str, n2: str) -> int:
        """Compare two integer strings"""
        if len(n1) < len(n2):
            return 1
        elif len(n1) > len(n2):
            return -1
        else:
            if n1 < n2:
                return 1
            elif n1 > n2:
                return -1
            else:
                return 0
