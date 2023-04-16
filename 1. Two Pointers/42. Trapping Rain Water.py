class Solution:
    """
    Approach 1: Dynamic Programming
    time: O(n), space: O(n)
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[0]] + [0]*(n-1)
        right_max = [0]*(n-1) + [height[n-1]]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            right_max[n-1-i] = max(right_max[n-1-i+1], height[n-1-i])
        res = sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
        return res


class Solution:
    """
    Approach 2: Monotonic Stack
    time: O(n), space: O(n)
    """
    def trap(self, height: List[int]) -> int:
        stack, res = [], 0
        for right, h_right in enumerate(height):
            while stack and h_right > height[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                fall = min(h_right, height[left]) - height[cur]
                width = right - left - 1
                res += fall * width
            stack.append(right)
        return res


class Solution:
    """
    Approach 3: Two Pointers
    time: O(n), space: O(1)
    """
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max, res = 0, 0, 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
