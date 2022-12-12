class Solution:
    """
    Approach 1: Slicing
    time: O(n), space: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        # Similar to: nums[0:k], nums[k:n] = nums[n-k:n], nums[0:n-k]


class Solution:
    """
    Approach 2: Circular Swaping by counting
    time: O(n), space: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        seen = set()
        count = 0
        i = 0
        tempi = nums[0]
        n = len(nums)

        while count < n:
            if i not in seen:
                j = (i+k) % n
                tempj = nums[j]
                nums[j] = tempi
                seen.add(i)
                i = j
                tempi = tempj
                count += 1
            else:
                i = (i+1) % n
                tempi = nums[i]


class Solution:
    """
    Approach 2.2: Circular Swaping by math
    time: O(n), space: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        times = self.gcd(n, k)
        i = 0
        start = 0
        tempi = nums[0]

        for _ in range(times):
            while True:
                j = (i+k) % n
                tempj = nums[j]
                nums[j] = tempi
                i = j
                tempi = tempj
                if i == start:
                    break
            i = (i+1) % n
            start = i
            tempi = nums[i]

    def gcd(self, a, b):
        """ method to compute greatest common divisor ( recursion ) """
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)


class Solution:
    """
    Approach 3: Flipping
    time: O(n), space: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[0:k] = nums[0:k][::-1]
        nums[k:n] = nums[k:n][::-1]
