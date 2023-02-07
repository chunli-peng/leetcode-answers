class Solution:
    """
    Approach 1: Two Heaps
    time: O((m+n)logm), O(m+nlogm) in Python since heapify() is O(m)
        where m=len(servers), n=len(tasks)
    space: O(m)
    """
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        busy = []  # pair: (available_time, index)
        idle = [(weight, i) for i, weight in enumerate(servers)]  # pair: (weight, index)
        heapq.heapify(idle)

        time = 0
        for j in range(len(tasks)):
            time = max(time, j)
            if not idle:
                time = busy[0][0]
            while busy and time >= busy[0][0]:
                _, i = heapq.heappop(busy)
                heapq.heappush(idle, (servers[i], i))
            _, i = heapq.heappop(idle)
            heapq.heappush(busy, (time+tasks[j], i))
            ans.append(i)
        return ans
