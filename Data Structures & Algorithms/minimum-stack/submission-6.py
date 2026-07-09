class MinStack:

    def __init__(self):
        self._items = []
        self._min_stack = []  # auxiliary stack to keep track of mins

    def push(self, val: int) -> None:
        self._items.append(val)
        # push to min stack if it's empty or val <= current min
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if self._items:
            val = self._items.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self) -> int:
        if self._items:
            return self._items[-1]
        return -1

    def getMin(self) -> int:
        if self._min_stack:
            return self._min_stack[-1]
        return float('inf')
