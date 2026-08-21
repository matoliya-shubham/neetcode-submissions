class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_v = min(self.min_stack[-1], val) if len(self.min_stack) > 0 else min(self.min_val, val)
        self.min_stack.append(min_v)
        # print(f'push: {self.stack}')
        # print(f'push: {self.min_stack}')

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        # print(f'pop: {self.stack}')
        # print(f'pop: {self.min_stack}')

    def top(self) -> int:
        # print(f'top: {self.stack}')
        # print(f'top: {self.min_stack}')
        return self.stack[-1]

    def getMin(self) -> int:
        # print(f'min: {self.stack}')
        # print(f'min: {self.min_stack}')
        return self.min_stack[-1]

