class Solution:
    """
    Approach 1: Monotonic Stack
    time: O(n), space: O(n)
    """
    def largestRectangleArea(self, heights: List[ int]) -> int:
        res = 0
        stack = []  # pair: [index,height]
        heights = heights + [0]
        # the ending zero could pop the all elements in the stack, avoiding iteration again

        for i_right, h_right in enumerate(heights):
            temp = i_right
            while stack and stack[-1][1] > h_right:
                i_left, h_left = stack.pop()
                res = max(res, h_left*(i_right-i_left))
                temp = i_left
            stack.append((temp, h_right))
        return res


class Solution:
    """
    Approach 1.2: Monotonic Stack (Alternative Code)
    time: O(n), space: O(n)
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights = [0] + heights + [0]
        # the ending zero could pop the all elements in the stack, avoiding iteration again
        # the leading zero could help to solve the situation of only one element in stack
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[temp])
            stack.append(i)
        return res
