#REVERSE INTEGER

class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        ans=0
        while x>0:
            sum=x%10
            ans=(ans*10) + sum
            x=x//10
        ans=ans*sign
        if (ans<=-2**31) or (ans>=2**(31)-1):
            return 0
        return ans       

        