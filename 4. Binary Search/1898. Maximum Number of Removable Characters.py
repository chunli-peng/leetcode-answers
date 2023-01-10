class Solution:
    """
    Approach 1: Binary Search
    time: O(nlogn), space: O(n)
    """
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        res = 0
        left, right = 0, len(removable)-1
        while left <= right:
            mid = (left + right)//2
            removed = set(removable[:mid+1])
            if self.check_subseq(s, p, removed):
                left = mid + 1
                res = max(res, left)
            else:
                right = mid - 1
        return res

    def check_subseq(self, s: str, p: str, removed: set) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if i in removed or s[i] != p[j]:
                i += 1
            else:
                i += 1
                j += 1
        return j == len(p)
