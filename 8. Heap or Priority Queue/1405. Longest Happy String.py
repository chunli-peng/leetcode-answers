class Solution:
    """
    Approach 1: Greedy + Max Heap
    time: O(C) for heapify() in Python,
        a+b+c times for heappush() and heappop() with O(logC)
        totally, O(C+(a+b+c)*logC), where C=3
    space: O(C)
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, max_heap = '', []
        for count, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                max_heap.append((count, ch))
        heapq.heapify(max_heap)

        while max_heap:
            count, ch = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not max_heap:
                    break
                count_2, ch_2 = heapq.heappop(max_heap)
                res += ch_2
                if count_2 < -1:
                    heapq.heappush(max_heap, (count_2+1, ch_2))
            else:
                res += ch
                count += 1
            if count:
                heapq.heappush(max_heap, (count, ch))
        return res


class Solution:
    """
    Approach 2: Greedy + Sorting
    time: O((a+b+c)*ClogC), space: O(C), where C=3
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        counter = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            counter.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (count, ch) in enumerate(counter):
                if count <= 0:
                    break
                if len(res) >= 2 and res[-2] == res[-1] == ch:
                    continue
                hasNext = True
                res += ch
                counter[i][0] -= 1
                break
            if not hasNext:
                return res
