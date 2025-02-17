class MinStack:
    def __init__(self):
        self.stack = []
        self.prevMinimun = []
        self.minimun = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimun = val

        self.stack.append(val)

        if val <= self.minimun:
            self.prevMinimun.append(self.minimun)
            self.minimun = val

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.minimun:
            self.minimun = self.prevMinimun.pop() if self.prevMinimun else None  # empty prevMinimun

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimun


# Example usage:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
