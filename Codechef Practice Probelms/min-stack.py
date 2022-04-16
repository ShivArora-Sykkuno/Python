class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val):
        if len(self.s) == 0:
            self.s.extend([val,val])
        else:
            self.s.extend([val, min(self.s[-1], val)])

    def pop(self):
        self.s.pop()
        self.s.pop()

    def top(self):
        return self.s[-2]

    def getMin(self):
        return self.s[-1]

    