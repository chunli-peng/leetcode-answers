class Solution:
    """
    Approach 1: Count
    time: O(|Σ|) for creating the key of the hash table, O(m) for counting,
        totally, O(n*(m+|Σ|)), where n=len(strs), m is average string length, Σ is character set.
    space: O(n*(m+|Σ|))
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = collections.defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for ch in string:
                counts[ord(ch)-ord("a")] += 1
            hashtable[tuple(counts)].append(string)
        return list(hashtable.values())


class Solution:
    """
    Approach 2: Sort
    time: O(nmlogm), where m is average string length
    space: O(nm)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = collections.defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            hashtable[key].append(string)

        return list(hashtable.values())
