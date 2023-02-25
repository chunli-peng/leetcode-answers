class Solution:
    """
    Approach 1: BFS + Hash Table
    time: O(b^d) for exhausting all combination, O(d) for yielding string.
            O(m) for initiating hash table.
        totally, O(b^d*d+m), where b is the decimal number, \
            d is the length of lock, m = len(deadends)
    space: O(b^d) for hash table <visited>, O(b^d) for <queue>,
        totally, O(b^d)
    """
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        queue = []
        visited = set(deadends)
        queue.append(['0000', 0])
        while queue:
            cur, res = queue.pop(0)
            if cur == target:
                return res
            for child in self._find_children(cur):
                if child not in visited:
                    visited.add(child)
                    queue.append([child, res+1])
        return -1

    def _find_children(self, cur):
        for i in range(4):
            digit = str((int(cur[i])+1) % 10)
            yield cur[:i]+digit+cur[i+1:]
            digit = str((int(cur[i])-1+10) % 10)
            yield cur[:i]+digit+cur[i+1:]
    # # Alternative code:
    # def _find_children(self, cur):
    #     res = []
    #     for i in range(4):
    #         digit = str((int(cur[i])+1) % 10)
    #         res.append(cur[:i]+digit+cur[i+1:])
    #         digit = str((int(cur[i])-1+10) % 10)
    #         res.append(cur[:i]+digit+cur[i+1:])
    #     return res


class Solution:
    """
    unfinished
    Approach 2: Heuristic Search (A* Algorithm)
    https://leetcode.cn/problems/open-the-lock/solutions/843687/da-kai-zhuan-pan-suo-by-leetcode-solutio-l0xo/
    """
    def openLock(self, deadends: List[str], target: str) -> int: