#IMPLEMENTING QUEUES USING STACKS

class MyQueue(object):

    def __init__(self):
        self.ini=[]
        self.out=[]

    def push(self, x):
        self.ini.append(x)
        
    def pop(self):
        self.transfer()
        if not self.out:
            return None
        return self.out.pop()            

    def peek(self):
        self.transfer()
        if not self.out:
            return None
        return self.out[-1]        
        

    def empty(self):
        return (not self.ini and not self.out)
        
    def transfer(self):
        if not self.out:
            while self.ini:
                self.out.append(self.ini.pop())        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()