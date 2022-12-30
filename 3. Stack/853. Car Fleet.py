class Solution:
    """
    Approach 1: Monotonic Stack + Sorting
    time: O(nlogn), space: O(n)
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # the time costs of car fleet leaders
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        for p, s in pair:
            time = (target-p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)
