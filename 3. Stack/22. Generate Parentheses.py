class Solution:
    """
    Approach 1: Stack + Backtrack
    time: O(4^2/sqrt(n)), more details in wiki Catalan number.
    space: O(n)
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(N_left=0, N_right=0):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            if N_left < n:
                stack.append("(")
                backtrack(N_left+1, N_right)
                stack.pop()
            if N_left > N_right:
                stack.append(")")
                backtrack(N_left, N_right+1)
                stack.pop()
        backtrack()
        return res


class Solution:
    """
    Approach 1: Recursion
    time: O(4^2/sqrt(n)), more details in wiki Catalan number.
    space: O(4^2/sqrt(n))
    details: 1. every legal string could be writen as "(a)b",
                where a and b are legal strings.
            2. generateParenthesis(num) calculate "a".
            3. generateParenthesis(n-1-num) calculate "b".
    """
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = []
        for num in range(n):
            for str_left in self.generateParenthesis(num):
                for str_right in self.generateParenthesis(n-1-num):
                    res.append('({}){}'.format(str_left, str_right))
        return res
