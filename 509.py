#FIBONACCI NUMBERS

class Solution(object):
    def fib(self, n):
        next=0
        a=0
        b=1    
        for i in range(n):
            next=a+b
            a=b
            b=next
        return a  
             