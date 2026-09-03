class MinStack:

    def __init__(self):
        # Main stack to hold all elements
        self.stack = []
        # Companion stack to hold the minimum value at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Determine the current minimum to push onto the min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Instant lookup in O(1) time
        return self.min_stack[-1]
