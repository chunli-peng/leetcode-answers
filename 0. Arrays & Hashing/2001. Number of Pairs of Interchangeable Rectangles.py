class Solution:
    """
    Approach 1: Hash Table
    time: O(n), space: O(n)
    """
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}  # {width/height: Count }
        res = 0

        for width, height in rectangles:
            # Increment the count for the ratio
            count[width/height] = 1 + count.get(width/height, 0)

        for count in count.values():
            res += (count * (count - 1)) // 2
        return res
