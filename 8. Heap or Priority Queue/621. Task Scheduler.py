class Solution:
    """
    Approach 1: Simulation
    time: O(|tasks|*|Σ|), where Σ is the set of task kind
    space: O(|Σ|)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        task_kinds = len(freq)
        next_valid_time = [1] * task_kinds  # initialization
        rest_tasks = list(freq.values())
        time = 0
        for _ in range(len(tasks)):
            time += 1
            min_next_valid = min(next_valid_time[i] for i in range(task_kinds)
                                 if rest_tasks[i] > 0)
            time = max(time, min_next_valid)  # check idle time
            best_task = -1  # compare with the minimum of rest_task
            for i in range(task_kinds):
                if rest_tasks[i] and next_valid_time[i] <= time \
                 and (best_task == -1 or rest_tasks[i] >= rest_tasks[best_task]):
                    best_task = i
            next_valid_time[best_task] = time + n + 1
            rest_tasks[best_task] -= 1
        return time


class Solution:
    """
    Approach 2: Matrix Construction
    time: O(|tasks|+|Σ|), where Σ is the set of task kind
    space: O(|Σ|)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Since every kind of task has same cooldown period, we could arrange tasks according to frequences
        freq = collections.Counter(tasks)
        max_exec = max(freq.values())
        max_exec_count = sum(1 for val in freq.values() if val == max_exec)
        # the last row of the matrix might be not full, \
        # the task with the max frequence will has additional round
        return max((max_exec-1)*(n+1) + max_exec_count , len(tasks))


class Solution:
    """
    Approach 3: Max Heap
    time: O(|tasks|) for Counter(),
        O(|Σ|) for heapify() in Python,
        |Σ| times for heappop() with O(log|Σ|),
        totally, O(|Σ|*log|Σ|+|tasks|)
    space: O(|Σ|)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # pairs of [-cnt, idle_time]
        while max_heap or queue:
            time += 1
            if not max_heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
