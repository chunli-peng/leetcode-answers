class Solution:
    """
    Approach 1: Sorting
    time: O(nlogn), space: O(n)
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v - x))
        return sorted(arr[:k])


class Solution:
    """
    Approach 2: Binary Search + Two Pointers
    time: O(logn+k), space: O(1)
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left+1: right]


class Solution:
    """
    Approach 3: Binary Search + Sliding Window
    time: O(logn), space: O(1)
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left+right)//2
            if x-arr[mid] > arr[mid+k]-x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]
