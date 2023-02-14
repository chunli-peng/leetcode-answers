class Solution:
    """
    Approach 1: Iteration
    time: O(mn), space: O(|Σ|), where Σ is alphabet set.
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_table = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words)-1):
            word_1, word_2 = words[i], words[i+1]
            for j in range(len(word_1)):
                if j == len(word_2):
                    return False
                if word_1[j] != word_2[j]:
                    if hash_table[word_1[j]] > hash_table[word_2[j]]:
                        return False
                    break
        return True


class Solution:
    """
    Approach 1.2: Iteration (alternative code)
    time: O(mn), space: O(|Σ|), where Σ is alphabet set.
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_table = {ch: i for i, ch in enumerate(order)}
        return all(s <= t for s, t in pairwise(
            [hash_table[ch] for ch in word] for word in words)
            )
