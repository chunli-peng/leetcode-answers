class Solution:
    """
    Approach 1: Recursive DFS in Multiway Tree
    time: O(4^n) for dfs()
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        res, n = [], len(digits)
        if not digits:
            return res

        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # # complete version:
        # def dfs(i=0, path=''):
        #     if i == n:
        #         res.append(path)  # No need for copy operations,
        #         # since <path> is not a compound object like list.
        #     else:
        #         for ch in hash_map[digits[i]]:
        #             path += ch
        #             dfs(i+1, path)
        #             path = path[:-1]

        # simplified version:
        def dfs(i=0, path=''):
            if i == n:
                res.append(path)
            else:
                for ch in hash_map[digits[i]]:
                    dfs(i+1, path+ch)
        dfs()
        return res


class Solution:
    """
    Approach 1.2: Recursive DFS in Multiway Tree (alternative code)
    time: O(4^n) for dfs()
    space: O(n) for function stack, O(n) for temporary variable <path>,
        totally, O(n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        res, n = [], len(digits)
        if not digits:
            return res

        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # # complete version:
        # def dfs(i=0, path=[]):
        #     if i == n:
        #         res.append(''.join(path))
        #     else:
        #         for ch in hash_map[digits[i]]:
        #             path.append(ch)
        #             dfs(i+1, path)
        #             path.pop()

        # simplified version:
        def dfs(i=0, path=[]):
            if i == n:
                res.append(''.join(path))
            else:
                for ch in hash_map[digits[i]]:
                    dfs(i+1, path+[ch])
        dfs()
        return res
