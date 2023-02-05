class Solution:
    """
    Approach 1: Min Heap + Sort
    time: O(nlogn) for sort(), n times heappop() and heappush() with O(logn)
        totally, O(nlogn)
    space: O(n)
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap = []  # pair: (target, num_pass)
        cur_pass = 0
        for in_pass, cur, target in trips:
            cur_pass += in_pass
            while min_heap and cur >= min_heap[0][0]:
                _, out_pass = heapq.heappop(min_heap)
                cur_pass -= out_pass
            if cur_pass > capacity:
                return False
            heapq.heappush(min_heap, (target, in_pass))
        return True


class Solution:
    """
    Approach 2: Array
    time: O(N), space: O(N), where N=1001
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta_pass = [0] * 1001

        for num, start, end in trips:
            delta_pass[start] += num
            delta_pass[end] -= num

        cur_pass = 0
        for num in delta_pass:
            cur_pass += num
            if cur_pass > capacity:
                return False
        return True


class Solution:
    """
    Approach 2.2: Array (Alternative Code)
    time: O(nlogn), space: O(n)
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta_pass = []
        for num, start, end in trips:
            delta_pass.append([start, num])
            delta_pass.append([end, -num])

        delta_pass.sort()

        cur_pass = 0
        for _, num in delta_pass:
            cur_pass += num
            if cur_pass > capacity:
                return False
        return True
