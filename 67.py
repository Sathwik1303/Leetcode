#ADD BINARY

class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        d=a+b
        c=f"{d:b}"
        return c