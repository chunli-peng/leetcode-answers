class Solution:
    """
    Approach 1: direct judgement
    time: O(n), space: O(1)
    """
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.alphanum(s[left]):
                left += 1
            while left < right and not self.alphanum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


class Solution:
    """
    Approach 2: built-in func
    time: O(n), space: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        if sgood == sgood[::-1]:
            return True
        return False
