#MAX CONSECUTIVE ONES

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        best=0
        curr=0
        for n in nums:
            if n==1:
                curr+=1
                if curr>best:
                    best=curr
            else:
                curr=0
        return best                
            