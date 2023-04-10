class Solution:
    """
    Aprroach 1: Brute Force
    time: O(n^2), space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        for num in set(nums):
            if nums.count(num) > target:
                return num


class Solution:
    """
    Aprroach 2: Hash Table
    time: O(n), space: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution:
    """
    Approach 3: Sort
    time: O(nlogn), space: O(logn) for function stack
    """
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class Solution:
    """
    Apprach 4: Randomization
    time: expect 2 times for probability 1/2, O(n) for check,
        totally, O(n)
    space: O(1)
    Follow-up requirement: time: O(n), space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        while True:
            res = random.choice(nums)
            if sum(1 for num in nums if num == res) > target:
                return res


class Solution:
    """
    Approach 5: Divide and Conquer
    time: T(n) = 2*T(n/2) + 2n, where T is the time complexity of problem.
        According to the Master Theorem, T(n) = O(nlogn)
    space: O(logn) for function stack
    """
    def majorityElement(self, nums: List[int]) -> int:
        def dfs(left, right):
            if left == right:
                return nums[left]
            mid = (right+left)//2
            res_left = dfs(left, mid)
            res_right = dfs(mid+1, right)
            if res_left == res_right:
                return res_left

            left_count = sum(1 for i in range(left, right+1) if nums[i] == res_left)
            right_count = sum(1 for i in range(left, right+1) if nums[i] == res_right)
            return res_left if left_count > right_count else res_right
        return dfs(0, len(nums)-1)


class Solution:
    """
    Approach 6: Boyer-Moore Voting Algorithm
    time: O(n), space: O(1)
    Follow-up requirement: time: O(n), space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        res, count = None, 0

        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res
