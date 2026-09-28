#SEPERATE THE DIGITS IN AN ARRAY

class Solution(object):
    def separateDigits(self, nums):
        new=[]
        for i in nums:
            dummy=[]
            while i>0:
                dummy.append(i%10)
                i//=10
            new.extend(dummy[::-1])    
        return new
