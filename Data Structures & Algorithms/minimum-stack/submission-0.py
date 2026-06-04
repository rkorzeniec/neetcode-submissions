class MinStack:

    def __init__(self):
        self.min_vals = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_vals) == 0 or val <= self.min_vals[-1]:
            self.min_vals.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        
        if val == self.min_vals[-1]:
            self.min_vals.pop()

        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
        
