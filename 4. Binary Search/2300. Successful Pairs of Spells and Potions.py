class Solution:
    """
    Approach 1: Sort + Binary Search
    time: O(nlogn) for sort(), where m=len(spells), n=len(potions),
        O(mlogn) for the search,
        totally, O((m+n)logn).
    space: O(1)
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)

        for sp in spells:
            left, right = 0, n-1
            counts = 0
            while left <= right:
                mid = (left+right) // 2
                if sp * potions[mid] >= success:
                    right = mid - 1
                    counts = n - mid
                else:
                    left = mid + 1
            res.append(counts)
        return res


class Solution:
    """
    Approach 1.2: Sort + Binary Search (Built-in Func)
    time: O(nlogn) for sort(), where m=len(spells), n=len(potions),
        O(mlogn) for the search,
        totally, O((m+n)logn).
    space: O(1)
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        return [n - bisect_right(potions, (success-1)//sp) for sp in spells]
