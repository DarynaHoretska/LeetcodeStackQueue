from collections import deque, defaultdict
class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.max_frequency = 0
        self.f_stk = defaultdict(deque)

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        if self.frequency[val] > self.max_frequency:
            self.max_frequency = self.frequency[val]
        self.f_stk[self.frequency[val]].append(val)

    def pop(self) -> int:
        val = self.f_stk[self.max_frequency].pop()
        self.frequency[val] -= 1
        if not self.f_stk[self.max_frequency]:
            self.max_frequency -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()