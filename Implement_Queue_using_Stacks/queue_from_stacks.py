class Stack:
    def __init__(self):
        self.elem = []

    def pop(self):
        return self.elem.pop()

    def push(self, value):
        self.elem.append(value)

    def peek(self):
        return self.elem[-1]

    def size(self):
        return len(self.elem)

    def is_empty(self):
        return len(self.elem) == 0

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()