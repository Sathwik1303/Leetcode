#PLUS ONE

class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in digits:
            num=num*10+i
        num+=1
        num=str(num)
        lis=[]
        for i in num: 
            lis.append(int(i))
        return lis    
        