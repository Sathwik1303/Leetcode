#POWER OF THREE

class Solution(object):
    def isPowerOfThree(self, n):
        if n==1 or n==3:
            return True
        x=3
        while x<=n:
            x*=3
            if x==n:
                return True
        return False

        