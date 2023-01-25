class Solution:
    """
    Approach 1: Binary Search
    time: O(log(m+n)), space: O(1)
    Requirement: time: O(log(m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """ get the k-th minimum """
            i, j = 0, 0
            while True:
                if i == m:
                    return nums2[j+k-1]
                if j == n:
                    return nums1[i+k-1]
                if k == 1:
                    return min(nums1[i], nums2[j])

                new_i = min(i+k//2-1, m-1)
                new_j = min(j+k//2-1, n-1)
                pivot_1, pivot_2 = nums1[new_i], nums2[new_j]
                if pivot_1 <= pivot_2:
                    k -= new_i-i+1
                    i = new_i+1
                else:
                    k -= new_j-j+1
                    j = new_j+1

        m, n = len(nums1), len(nums2)
        total_len = m+n
        if total_len % 2 == 1:  # odd
            return getKthElement((total_len+1)//2)
        else:  # even
            return (getKthElement(total_len//2) + getKthElement(total_len//2+1)) / 2



class Solution:
    """
    Approach 2: Binary Search + Partition
    time: O(log(min(m, n))), space: O(1)
    Requirement: time: O(log(m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = m+n
        left, right = 0, m-1
        while True:
            i = (left+right)//2
            j = total_len//2-i-2

            # the maximums of the left set
            nums1_left = nums1[i] if i >= 0 else float('-inf')
            nums2_left = nums2[j] if j >= 0 else float('-inf')
            # the minimums of the right set
            nums1_right = nums1[i+1] if (i+1) < m else float('inf')
            nums2_right = nums2[j+1] if (j+1) < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # partition is correct
                if total_len % 2:  # odd
                    return min(nums1_right, nums2_right)
                else:  # even
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i-1
            else:
                left = i+1
