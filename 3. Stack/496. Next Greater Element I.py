class Solution:
    """
    Approach 1: Brute Force
    time: O(mn), space: O(1)
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        ans = [-1] * m
        for i in range(m):
            j = nums2.index(nums1[i])
            k = j + 1
            while k < n and nums2[k] < nums2[j]:
                k += 1
            if k < n:
                ans[i] = nums2[k]
        return ans


class Solution:
    """
    Approach 2: Monotonic Stack
    time: O(m+n), space: O(n), where n = len(nums)
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashtable = {}
        stack = []  # desending order
        for num in nums2:
            while stack and stack[-1] < num:
                hashtable[stack.pop()] = num
            stack.append(num)
        return [hashtable.get(num, -1) for num in nums1]
