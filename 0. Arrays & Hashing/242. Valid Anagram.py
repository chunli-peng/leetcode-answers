class Solution:
    """
    Approach 1: Sort
    time: O(nlogn), space: O(logn)
    Follow-up requirement: What if the inputs contain Unicode characters? \
        How would you adapt your solution to such a case?
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return True if sorted(s) == sorted(t) else False


class Solution:
    """
    Approach 2: Hash Table
    time: O(n), space: O(|Σ|), where Σ is the character set.
    Follow-up requirement: What if the inputs contain Unicode characters? \
        How would you adapt your solution to such a case?
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtable_s, hashtable_t = {}, {}
        for i in s:
            if i not in hashtable_s:
                hashtable_s[i] = 0
            hashtable_s[i] += 1
        for j in t:
            if j not in hashtable_t:
                hashtable_t[j] = 0
            hashtable_t[j] += 1
        return hashtable_t == hashtable_t


class Solution:
    """
    Approach 2.2: Hash Table (Built-in Func)
    time: O(n), space: O(|Σ|), where Σ is the character set.
    Follow-up requirement: What if the inputs contain Unicode characters? \
        How would you adapt your solution to such a case?
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return True if Counter(s) == Counter(t) else False
