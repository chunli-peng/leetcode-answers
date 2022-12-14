class Solution:
    """
    Approach 1: Two Pointers
    time: O(n), space: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height)-1, 0
        while left < right:
            area = max(area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
