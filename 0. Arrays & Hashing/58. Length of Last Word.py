class Solution:
    """
    Approach 1: Reverse Iteration
    time: O(n), space: O(1)
    """
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i > 0 and s[i] == ' ':
            i -= 1
        res = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            res += 1
        return res


class Solution:
    """
    Approach 2: Split and Strip (Built-in Func)
    time: O(n), space: O(n)
    """
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.strip().split(" ")
        return len(word_list[-1])
