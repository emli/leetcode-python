# time: O(1) for all operations in average
# space: O(N) where N is the maximum size of the queue
class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        self.checkForEmpty()
        return self.second.pop()

    def checkForEmpty(self):
        if len(self.second) == 0:
            self.moveFromFirstToSecond()

    def moveFromFirstToSecond(self):
        while len(self.first) > 0:
            self.second.append(self.first.pop())

    def peek(self) -> int:
        self.checkForEmpty()
        return self.second[-1]

    def empty(self) -> bool:
        return len(self.first) == 0 and len(self.second) == 0
