#POWER OF FOUR

class Solution(object):
    def isPowerOfFour(self, n):
        ans=1
        if n==1:
            return True
        while (ans<=n):
            ans*=4
            if ans==n:
                return True
        return False        
        