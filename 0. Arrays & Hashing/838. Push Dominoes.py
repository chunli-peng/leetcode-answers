class Solution:
    """
    Approach 1: Simulation
    time: O(n), space: O(n)
    """
    def pushDominoes(self, dominoes: str) -> str:
        res = list(dominoes)
        n = len(res)
        queue = deque()  # use list: [] might cause: Time Limit Exceeded

        # the initial states of "L" and "R" will keep unchanged.
        for i, dom in enumerate(res):
            if dom != '.':
                queue.append((i, dom))

        # Simulation:
        while queue:
            i, dom = queue.popleft()
            if dom == 'L':
                if i > 0 and res[i-1] == '.':
                    res[i-1] = 'L'
                    queue.append((i-1, 'L'))
            else:
                if i+1 < n and res[i+1] == '.':
                    if i+2 < n and res[i+2] == 'L':  # when conflict
                        queue.popleft()  # pop (i+2, 'L)
                    else:
                        res[i+1] = 'R'
                        queue.append((i+1, 'R'))
        return ''.join(res)
