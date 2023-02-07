class Solution:
    """
    Approach 1: Sorting + Min Heap
    time: O(nlogn) for sorted, n times O(logn) for heappop and heappush
        totally, O(nlogn)
    space: O(n)
    """
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        res, min_heap = [], []
        i, n = 0, len(tasks)
        time = tasks[0][0]

        while len(res) < n:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if min_heap:
                delta_t, task_i = heapq.heappop(min_heap)
                time += delta_t
                res.append(task_i)
            else:
                time = tasks[i][0]
        return res


