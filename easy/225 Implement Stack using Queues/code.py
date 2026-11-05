class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        self.q1.append("")
        for i in range(len(self.q1) - 1, -1, -1):
            self.q1[i] = self.q1[i - 1]
        self.q1[0] = x

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
