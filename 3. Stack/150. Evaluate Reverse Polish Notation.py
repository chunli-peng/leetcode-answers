class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda x, y: int(x/y)
        }
        stack = []
        for ch in tokens:
            try:
                num = int(ch)
            except ValueError:
                num_2 = stack.pop()
                num_1 = stack.pop()
                num = operations[ch](num_1, num_2)
            finally:
                stack.append(num)
        return stack[0]
