class Solution:
    """
    Approach 1: Greedy (Two Pointer)
    time: O(nlogn), space: O(logn) for sorting
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1  # non-shared boat
            else:
                light += 1  # shared boat
                heavy -= 1
            res += 1
        return res
