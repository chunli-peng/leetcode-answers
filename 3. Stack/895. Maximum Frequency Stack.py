class FreqStack:
    """
    Approach 1: Hash Table + Stack
    time: O(1), space: O(n)
    """
    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
