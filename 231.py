#POWER OF TWO

class Solution(object):
    def isPowerOfTwo(self, n):
        x=2
        if n==1 or n==2:
            return True
        while x<=n:
            x*=2
            if x==n:
                return True
        return False        

        