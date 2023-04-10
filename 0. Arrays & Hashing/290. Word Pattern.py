class Solution:
    """
    Approach 1: Two Hash Tables
    time: O(n), space: O(|Σ|), where Σ is the character set
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        len_p, len_w = len(pattern), len(words)
        if len_p != len_w:
            return False

        p_to_w, w_to_p = {}, {}
        for ch, word in zip(pattern, words):
            if (ch in p_to_w and p_to_w[ch] != word) or \
             (word in w_to_p and w_to_p[word] != ch):
                return False
            p_to_w[ch], w_to_p[word] = word, ch
        return True


class Solution:
    """
    Approach 2: Index
    time: O(n), space: O(1)
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        len_p, len_w = len(pattern), len(words)
        if len_p != len_w:
            return False

        for ch, word in zip(pattern, words):
            if pattern.index(ch) != words.index(word):
                # index() will return the fist index of input
                return False
        return True
