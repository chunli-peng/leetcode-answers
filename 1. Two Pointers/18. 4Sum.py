class Solution:
    """
    The solution of this problem is similar to problem 15. 3Sum
    Approach 1: Sorting + Two Pointers
    time: O(n^3),
    space: O(logn) for Sorting (if original nums could be revised.
    without considering the space of the answer)
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, sol = len(nums), []
        nums.sort()

        if len(nums) < 4:
            return sol  # 1 <= nums.length <= 200

        for p1 in range(n-3):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            if nums[p1] + nums[p1+1] + nums[p1+2] + nums[p1+3] > target:  # pruning
                break
            if nums[p1] + nums[n-3] + nums[n-2] + nums[n-1] < target:  # pruning
                continue

            for p2 in range(p1+1, n-2):
                if p2 > p1+1 and nums[p2] == nums[p2-1]:
                    continue
                if nums[p1] + nums[p2] + nums[p2+1] + nums[p2+2] > target:
                    break
                if nums[p1] + nums[p2] + nums[n-2] + nums[n-1] < target:
                    continue

                p3, p4 = p2+1, n-1

                while p3 < p4:
                    sum_4 = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if sum_4 > target:
                        p4 -= 1
                    elif sum_4 < target:
                        p3 += 1
                    else:
                        sol.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        while p3 < p4 and nums[p3] == nums[p3+1]:
                            p3 += 1
                        p3 += 1
                        while p3 < p4 and nums[p4] == nums[p4-1]:
                            p4 -= 1
                        p4 -= 1
        return sol
