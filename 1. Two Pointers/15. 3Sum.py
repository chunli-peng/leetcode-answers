class Solution:
    """
    Approach 1: Sorting + Two Pointers
    time: O(n^2),
    space: O(logn) for Sorting (if original nums could be revised.
    without considering the space of the answer)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, sol = len(nums), []
        nums.sort()

        for p1 in range(n-2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            if nums[p1] + nums[p1+1] + nums[p1+2] > 0:  # pruning
                break
            if nums[p1] + nums[n-2] + nums[n-1] < 0:  # pruning
                continue
            p2, p3 = p1+1, n-1
            while p2 < p3:
                sum_3 = nums[p1] + nums[p2] + nums[p3]
                if sum_3 > 0:
                    p3 -= 1
                elif sum_3 < 0:
                    p2 += 1
                else:
                    sol.append([nums[p1], nums[p2], nums[p3]])
                    while p2 < p3 and nums[p2] == nums[p2+1]:
                        p2 += 1
                    p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3-1]:
                        p3 -= 1
                    p3 -= 1
        return sol
