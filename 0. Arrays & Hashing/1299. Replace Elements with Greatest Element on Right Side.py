class Solution:
    """
    Approach 1: Reverse Iteration
    time: O(n), space: O(1)
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = max(arr[i], right_max)
            arr[i] = right_max
            right_max = temp
        return arr
