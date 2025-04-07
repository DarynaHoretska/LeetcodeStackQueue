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
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def top(self) -> int:
        

    def empty(self) -> bool:
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()