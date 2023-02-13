class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(n^2) for dfs(), space: O(n) for function stack
    """
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i=0, prev=None):
            if i == len(s):
                return True

            for j in range(i, n):
                if prev-1 == int(s[i:j+1]) and dfs(j+1, int(s[i:j+1])):
                    return True
            return False

        for j in range(n-1):
            if dfs(j+1, int(s[:j+1])):
                return True
        return False


class Solution:
    """
    Approach 1.2: Recursive DFS in Multiway Tree (alternative code)
    time: O(n^2) for dfs(), space: O(n) for function stack
    """
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i=0, prev=None):
            if i == len(s):
                return True
            if prev is None:  # cannot write (if not prev) since situation: prev=0
                for j in range(n-1):
                    if dfs(j+1, int(s[:j+1])):
                        return True
            else:
                for j in range(i, n):
                    if prev-1 == int(s[i:j+1]) and dfs(j+1, int(s[i:j+1])):
                        return True
            return False
        return dfs()


class Solution:
    """
    Approach 2: Iteration
    time: O(n^2), space: O(1)
    """
    def splitString(self, s: str) -> bool:
        n, start_val = len(s), 0

        for i in range(n-1):
            start_val = 10 * start_val + int(s[i])
            prev_val, curr_val = start_val, 0
            curr_i = i+1

            for j in range(i+1, n):
                if prev_val == 1:
                    if all(s[k] == '0' for k in range(curr_i, n)):
                        return True
                    else:
                        break

                curr_val = 10 * curr_val + int(s[j])
                if curr_val > prev_val-1:
                    break
                elif curr_val == prev_val-1:
                    if j + 1 == n:
                        return True
                    prev_val = curr_val
                    curr_val = 0
                    curr_i = j+1
        return False
