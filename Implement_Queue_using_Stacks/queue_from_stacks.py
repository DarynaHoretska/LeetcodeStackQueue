class Queue:
    def __init__(self):
        self.elem = []

    def pop(self):
        return self.elem.pop(0)

    def push(self, value):
        self.elem.append(value)

    def peek(self):
        return self.elem[0]

    def size(self):
        return len(self.elem)

    def is_empty(self):
        return len(self.elem) == 0

class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue1.push(x)

    def pop(self) -> int:
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        el = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return el

    def top(self) -> int:
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        el = self.queue1.pop()
        self.queue2.push(el)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return el

    def empty(self) -> bool:
        return self.queue1.is_empty() and self.queue2.is_empty()


# Your Myqueue object will be instantiated and called as such:
# obj = Myqueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()