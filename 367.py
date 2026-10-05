#VALID PERFECT SQUARE

class Solution(object):
    def isPerfectSquare(self, num):
        i=1
        ans=1
        while (ans<=num):
            ans=i*i
            if ans==num:
                return True
            i+=1
        return False
        