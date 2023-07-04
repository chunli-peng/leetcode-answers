class Solution:
    """
    Approach 1: Horizontal Scan
    time: O(mn), space: O(1)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(count):
            prefix = self.get_common_prefix(prefix, strs[i])
        return prefix

    def get_common_prefix(self, str_1, str_2):
        length, i = min(len(str_1), len(str_2)), 0
        while i < length and str_1[i] == str_2[i]:
            i += 1
        return str_1[:i]


class Solution:
    """
    Approach 2: Vertical Scan
    time: O(mn), space: O(1)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length, count = len(strs[0]), len(strs)
        for i in range(min_length):
            ch = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:i]
        return strs[0]


class Solution:
    """
    Approach 3: Divide and Conquer
    time: O(mn)
    space: O(mlongn), where m is average string length, n=len(strs)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcp_left, lcp_right = lcp(start, mid), lcp(mid+1, end)
            min_length = min(len(lcp_left), len(lcp_right))
            for i in range(min_length):
                if lcp_left[i] != lcp_right[i]:
                    return lcp_left[:i]
            return lcp_left[:min_length]

        return "" if not strs else lcp(0, len(strs)-1)


class Solution:
    """
    Approach 4: Binary Search
    time: O(mnlogm), where m is minimal string length, n=len(strs)
    space: O(1)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def is_common_prefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        low, high = 0, min_length
        while low < high:
            mid = (high+low+1) // 2
            if is_common_prefix(mid):
                low = mid
            else:
                high = mid-1
        return strs[0][:low]


class Solution:
    """
    Approach 5: Trie
    time: O(mn), space: O(mn)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:
            return ''

        trie = []  # [{}, ...]
        min_index = float('')
        for word in strs:
            for i, ch in enumerate(word):
                if len(trie) <= i:
                    trie.append(set(ch))
                elif ch in trie[i]:
                    continue
                else:
                    min_index = min(min_index, i)
            min_index = min(min_index, i+1)
        return strs[0][:min_index]
