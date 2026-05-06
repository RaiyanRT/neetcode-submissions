class MinStack:
    #Ill have two stacks one is min stack and one is the normal stack, everrytime i do a push i will compare to the last 
    # element of the stack and if it is smaller ill pop it in
    def __init__(self):
        # the normal stack
        # the minimum stack where top value is always the smallest
        self.stack = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        

        if not self.min_stack:
            self.min_stack.append(val)
            self.stack.append(val)
            return

        current_min = self.min_stack[-1]

        if self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(current_min)

        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        
