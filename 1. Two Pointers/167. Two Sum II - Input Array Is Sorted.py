class Solution:
    """
    Approach 1: Binary Search
    time: O(nlogn), space: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            left, right = i+1, n-1
            while left <= right:
                mid = (left+right)//2
                if numbers[mid] == target - numbers[i]:
                    return [i+1, mid+1]  # 1-indexed array
                elif numbers[mid] > target - numbers[i]:
                    right = mid - 1
                else:
                    left = mid + 1


class Solution:
    """
    Approach 2: Two Pointers
    time: O(n), space: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1, right+1]  # 1-indexed array
            elif cur_sum <= target:
                left += 1
            else:
                right -= 1
