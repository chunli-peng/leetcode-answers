class Solution:
    """
    Approach 1: Binary Search + Greedy
    time: O(nlogn) for sort(), O(nlogM) for binary search, where M = max(nums),
        totally, O(nlogn+nlogM)
    space: O(1)
    """
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        def is_valid(threshold):
            # greedy
            i, cnt = 0, 0
            while i < len(nums)-1:
                if nums[i+1]-nums[i] <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        # binary search
        nums.sort()
        left, right = 0, nums[-1]
        res = nums[-1]

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
