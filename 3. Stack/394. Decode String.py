class Solution:
    """
    Approach 1: Stack
    time: O(n), space: O(n)
    """
    def decodeString(self, s: str) -> str:
        stack, multi, res = [], 0, ''
        for ch in s:
            if ch == '[':
                stack.append([multi, res])
                multi, res = 0, ''
            elif ch == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= ch <= '9':
                multi = multi*10 + int(ch)
            else:
                res += ch
        return res


class Solution:
    """
    Approach 2: Recursion
    time: O(n), space: O(n)
    """
    def decodeString(self, s: str) -> str:
        def dfs(i=0):
            multi, res = 0, ''
            while i < len(s):
                ch = s[i]
                if ch == '[':
                    i, temp = dfs(i+1)
                    res += multi * temp
                    multi = 0
                elif ch == ']':
                    return i, res  # return the intermediate result
                elif '0' <= ch <= '9':
                    multi = multi * 10 + int(ch)
                else:
                    res += ch
                i += 1
            return res  # return the final result
        return dfs()
