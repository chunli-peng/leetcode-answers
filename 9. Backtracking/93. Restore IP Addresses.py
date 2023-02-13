class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(d^m) for dfs(), where d is max digits, m is the max numbers of integer,
        O(m) for check valid, totally, O(m*d^m), where m=4, d=3
    space: O(m) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, n = [], len(s)
        if n > 12:
            return res
        # # complete version:
        # def dfs(i=0, dots=0, path=''):
        #     if dots == 4 and i == n:
        #         res.append(path[:-1])
        #         return
        #     if dots > 4:
        #         return
        #     for j in range(i, min(i+3, n)):
        #         if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
        #             path += s[i:j+1]+'.'
        #             dfs(j+1, dots+1, path)
        #             path = path[:-(j+2-i)]

        # simplified version:
        def dfs(i=0, dots=0, path=''):
            if dots == 4 and i == n:
                res.append(path[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, n)):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
                    dfs(j+1, dots+1, path+s[i:j+1]+'.')
        dfs()
        return res
