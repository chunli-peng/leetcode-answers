class Solution:
    """
    Approach 1: Hash Table
    time: O(mn), space: O(mn)
    """
    def leastBricks(self, wall: List[List[int]]) -> int:
        m, n = sum(wall[0]), len(wall)
        gap_counter = {m: -n}  # {gap position: counts}

        for row in wall:
            cut = 0  # Position
            for brick in row:
                cut += brick
                gap_counter[cut] = 1 + gap_counter.get(cut, 0)
        return n - max(gap_counter.values())  # Total number of rows - Max gap
