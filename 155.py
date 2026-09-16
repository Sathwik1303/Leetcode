#MIN STACK
'''
I SOLVED THIS WHOLE QUESTION USING LOOPS AND THAT WAS CORRECT BUT I WAS OF
TIME COMPLEXITY O(N) BUT THEN I CHANGED SOME PART OF THE CODE AND THEN
CONVERTED TO O(1).
'''

class MinStack(object):

    def __init__(self):
        self.list = []
        self.min_stack = []

    def push(self, value):
        self.list.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if len(self.list) == 0:
            return None
        self.min_stack.pop()
        return self.list.pop()

    def top(self):
        if len(self.list) == 0:
            return None
        return self.list[-1]

    def getMin(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]