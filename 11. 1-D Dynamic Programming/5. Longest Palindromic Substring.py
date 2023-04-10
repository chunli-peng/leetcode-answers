class Solution:
    """
    Approach 1: Center Extension Method
    time: O(n^2), space: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self._expand_center(s, i, i)
            left2, right2 = self._expand_center(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def _expand_center(self, s, left, right):
        """Expand the string and return the index."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1


class Solution:
    """
    Approach 2: Manacher Algorithm
    time: O(n), space: O(n)
    """
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, -1
        s = '#' + '#'.join(list(s)) + '#'  # translate to odd string
        arm_len_list = []
        right = -1  # right end of the string
        j = -1  # center of palindrome string
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i  # symmetry point of <i>
                min_arm = min(arm_len_list[i_sym], right-i)
                cur_arm = self._expand_center(s, i-min_arm, i+min_arm)
            else:
                cur_arm = self._expand_center(s, i, i)
            arm_len_list.append(cur_arm)
            if i + cur_arm > right:
                j, right = i, i + cur_arm  # update
            if 2 * cur_arm + 1 > end - start:
                start, end = i-cur_arm, i+cur_arm
        return s[start+1:end+1:2]  # skip the '#'

    def _expand_center(self, s, left, right):
        """Expand the string and return the arm length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2
