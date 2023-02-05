class Solution:
    """
    Approach 1: Greedy + Max Heap
    time: O(n) for Counter(), O(|Σ|) for heapify() in Python,
        n times O(log|Σ|) for heappop() and heappush()
        totally, O(nlog|Σ|+|Σ|)
    space: O(|Σ|)
    """
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        counts = collections.Counter(s)
        max_count = max(counts.items(), key=lambda x: x[1])[1]
        if max_count > (n+1)//2:
            return ''

        max_heap = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(max_heap)
        res = ''

        while len(max_heap) > 1:
            count_1, ch_1 = heapq.heappop(max_heap)
            count_2, ch_2 = heapq.heappop(max_heap)
            res += ch_1
            res += ch_2
            if count_1 < -1:
                heapq.heappush(max_heap, (count_1+1, ch_1))
            if count_2 < -1:
                heapq.heappush(max_heap, (count_2+1, ch_2))
        if max_heap:
            res += max_heap[0][1]
        return res


class Solution:
    """
    Approach 2: Greedy + Counter
    time: O(n) for Counter(), O(n+|Σ|) for interation, totally, O(n+|Σ|)
    space: O(|Σ|)
    """
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        counts = collections.Counter(s)
        max_count = max(counts.items(), key=lambda x: x[1])[1]
        if max_count > (n+1)//2:
            return ''

        res = [''] * n
        even_i, odd_i = 0, 1

        for ch, count in counts.items():
            while 0 < count <= n//2 and odd_i < n:
                res[odd_i] = ch
                count -= 1
                odd_i += 2
            while count > 0:
                res[even_i] = ch
                count -= 1
                even_i += 2
        return ''.join(res)
