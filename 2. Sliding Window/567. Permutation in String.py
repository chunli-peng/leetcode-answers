class Solution:
    """
    Approach 1: Sliding Window
    time: O(m+n), where m, n are lengths of the strings s1 and s2.
    space: O(∣Σ∣), where ∣Σ∣ is the distinct character numbers in s1.
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_1, len_2 = len(s1), len(s2)
        if len_1 > len_2:
            return False

        left, right = 0, len_1-1
        counter_1 = collections.Counter(s1)
        counter_2 = collections.Counter(s2[:right])
        while right < len_2:
            counter_2[s2[right]] += 1
            if counter_1 == counter_2:
                return True
            counter_2[s2[left]] -= 1
            if counter_2[s2[left]] == 0:
                del counter_2[s2[left]]
            left += 1
            right += 1
        return False
