class Solution:
    """
    Approach 1: Sorting
    time: O(nlogn), space: O(logn)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]


class Solution:
    """
    Approach 2: Max Heap
    time: O(nlogk), space: O(k)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(max_heap)

        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(max_heap, (dist, i))

        res = [points[i] for (_, i) in max_heap]
        return res


class Solution:
    """
    Approach 3: QuickSelect
    time: O(nlogk), space: O(k)
    unfinished
    https://leetcode.cn/problems/k-closest-points-to-origin/solutions/477916/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


    def _dis(self, x, y) -> int:
        """Return the square of Euclidean distance"""
        return x**2 + y**2

