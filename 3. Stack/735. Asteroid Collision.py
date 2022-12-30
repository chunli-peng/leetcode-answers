class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(1)
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                alive = stack[-1] + ast < 0
                if stack[-1] + ast <= 0:
                    stack.pop()
            if alive:
                stack.append(ast)
        return stack
