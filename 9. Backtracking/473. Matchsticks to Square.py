class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(nlogn) for sort(), O(4^n) for dfs(), totally, O(4^n)
    space: O(n) for function stack, O(n) for temporary variable <sides>,
        totally, O(n)
    """
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        n, sq_len = len(matchsticks), sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def dfs(i=0, sides=[0]*4):
            if i == n:
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= sq_len:
                    sides[j] += matchsticks[i]
                    if dfs(i+1, sides):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return dfs()


class Solution:
    """
    unfinished
    Approach 2: Bitmask Dynamic Programming
    time: O(n*2^n)
    space: O(2^n) for the variable <dp>
    https://leetcode.com/problems/matchsticks-to-square/solutions/164059/matchsticks-to-square/
    https://leetcode.cn/problems/matchsticks-to-square/solutions/1528435/huo-chai-pin-zheng-fang-xing-by-leetcode-szdp/
    """
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sq_len = sum(matchsticks) // 4
        if sum(matchsticks) % 4:
            return False
        matchsticks.sort(reverse=True)
