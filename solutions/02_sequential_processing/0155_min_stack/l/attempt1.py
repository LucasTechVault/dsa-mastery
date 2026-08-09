class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        
    def push(self, value: int) -> None:
        # main stack always gets value
        self.main_stack.append(value)
        
        # min stack needs check
            # 1. if min stack is empty
            # 2. if current value is smaller (or equals) to min_stack (to handle duplicates min val)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        
    def pop(self) -> None:
        main_popped = self.main_stack.pop()
        
        # point where min value was appended, need to remove as well
        if main_popped == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self) -> int:
        return self.main_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        