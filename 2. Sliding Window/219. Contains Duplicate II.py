class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n)
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}  # pair: {num: index}
        for i, num in enumerate(nums):
            if num in visited and i - visited[num] <= k:
                return True
            visited[num] = i
        return False


class Solution:
    """
    Approach 2: Sliding Window
    time: O(n), space: O(k)
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        for right in range(len(nums)):
            if right-left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
