class Solution:
    """
    Approach 1: Sliding Window
    time: O(n), space: O(k)
    """
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window = sum(arr[:k-1])

        for left in range(len(arr)-k+1):
            window += arr[left+k-1]
            if window >= threshold*k:
                res += 1
            window -= arr[left]
        return res
