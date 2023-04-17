class Solution:
    """
    Approach 1: Sort
    time: O(logm) for each string, O(nlogn) for comparing strings with O(logm) of cmp(),
        O(nlogm) for joining strings, where m is the maximum of 32 bits integer
        totally, O(n*logm+nlogn*logm+nlogm) = O(nlogn*logm)
    space: O(logn) for function stack, O(nlogm) for <strs>
        totally, O(logn+nlogm)
    """
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)

        def cmp(a: str, b: str):
            """Compare <a> and <b> by joing strings """
            if a+b == b+a:
                return 0
            elif a+b > b+a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'
