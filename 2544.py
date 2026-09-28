#ALTERNATING DIGIT SUM

class Solution(object):
    def alternateDigitSum(self, n):
        reverse=0
        while n>0:
            reverse=reverse*10+(n%10)
            n//=10
        pos=0
        sign=1
        while reverse>0:
            pos+=sign*(reverse%10)
            sign=-sign
            reverse//=10
        return pos
