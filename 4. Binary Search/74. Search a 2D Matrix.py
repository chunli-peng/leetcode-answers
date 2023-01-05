class Solution:
    """
    Approach 1: Double Binary Search
    time: O(logm+logn)=O(logmn), space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        row = (top + bottom) // 2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True
        return False


class Solution:
    """
    Approach 2: Global Binary Search
    time: O(logmn), space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows*cols-1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True
        return False
