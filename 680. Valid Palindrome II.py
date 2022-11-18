class Solution:
    """
    Approach 1: Greedy
    time: O(n), space: O(1)
    """
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.check_palindrome(s, i+1, j) or self.check_palindrome(s, i, j-1)
        return True

    def check_palindrome(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


class Solution:
    """
    Approach 1.2: Python Slicing
    time: O(n), space: O(1)
    """
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if (s[i+1:j+1] == s[i+1:j+1][::-1]) or (s[i:j] == s[i:j][::-1]):
                    return True
                return False
        return True
