class Solution:
    """
    Approach 1: BFS + Hash Table
    time: O(m*n) for create <graph>, O(m*n) for bfs(), O(n) for each string,
        totally, O(m*n^2), m=len(wordList), n=len(beginWord)
    space: O(m*n^2) for <graph>, where O(mn) for all nodes with O(n) length,
        O(mn) for <visited> and <queue>, totally, O(m*n^2)
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + '.' + word[i+1:]
                graph[pattern].append(word)

        queue = [(beginWord, 1)]
        visited = set([beginWord])
        while queue:
            word, res = queue.pop(0)
            if word == endWord:
                return res
            for i in range(n):
                pattern = word[:i] + '.' + word[i+1:]
                for child in graph[pattern]:
                    if child not in visited:
                        queue.append([child, res+1])
                        visited.add(child)
        return 0


class Solution:
    """
    Approach 2: Bidirectional BFS + Hash Table
    time: O(m*n) for create <graph>, O(m*n) for bfs(), O(n) for each string,
        totally, O(m*n^2), m=len(wordList), n=len(beginWord)
    space: O(m*n^2) for <graph>, where O(mn) for all nodes with O(n) length,
        O(mn) for <visited> and <queue>, totally, O(m*n^2)
    """
    def __init__(self):
        self.n = 0
        self.graph = collections.defaultdict(list)

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        self.n = len(beginWord)
        for word in wordList:
            for i in range(self.n):
                pattern = word[:i] + "." + word[i+1:]
                self.graph[pattern].append(word)

        queue_begin = [beginWord]  # BFS starting from beginWord
        queue_end = [endWord]  # BFS starting from endWord

        visited_begin = {beginWord : 1}  # pair: word: level
        visited_end = {endWord : 1}  # pair: word: level
        res = 0

        while queue_begin and queue_end:
            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                res = self.bfs(queue_begin, visited_begin, visited_end)
            else:
                res = self.bfs(queue_end, visited_end, visited_begin)
            if res:
                return res
        return 0

    def bfs(self, queue, visited, others_visited):
        queue_len = len(queue)
        for _ in range(queue_len):
            word = queue.pop(0)
            for i in range(self.n):
                pattern = word[:i] + "." + word[i+1:]
                for child in self.graph[pattern]:
                    if child in others_visited:
                        return visited[word] + others_visited[child]
                    if child not in visited:
                        visited[child] = visited[word] + 1
                        queue.append(child)
