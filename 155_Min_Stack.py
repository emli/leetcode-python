#space : O(N)
class MinStack:

    def __init__(self):
        self.stack = []

    # time : O(1) on average
    def push(self, x: int) -> None:
        minElement = x if (len(self.stack) == 0) else self.stack[-1][1]
        self.stack.append((x, min(minElement, x)))

    # time : O(1)
    def pop(self) -> None:
        self.stack.pop()

    # time : O(1)
    def top(self) -> int:
        return self.stack[-1][0]

    # time : O(1)
    def getMin(self) -> int:
        return self.stack[-1][1]