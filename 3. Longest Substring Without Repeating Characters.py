class Solution:
    """
    Approach 1: Sliding Window
    time: O(n),
    space: O(|Σ|), where |Σ| is the number of distinct characters in the string.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable, n = set(), len(s)
        right, res = 0, 0
        for left in range(n):
            if left != 0:
                hashtable.remove(s[left-1])
            while right < n and s[right] not in hashtable:
                hashtable.add(s[right])
                right += 1
            res = max(res, right-left)
        return res


class Solution:
    """
    Approach 1.2: Sliding Window + Hashmap
    time: O(n),
    space: O(|Σ|), where |Σ| is the number of distinct characters in the string.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = -1, 0
        c_dict = {}  # the newest indices of the characters
        for right, c_right in enumerate(s):
            if c_right in c_dict and c_dict[c_right] > left:
                left = c_dict[c_right]  # the new left point of the window
                c_dict[c_right] = right  # update the newest index
            else:
                c_dict[c_right] = right
                res = max(res, right-left)
        return res
