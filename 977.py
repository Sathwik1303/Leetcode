#SQUARES OF SORTED ARRAY

class Solution(object):
    def sortedSquares(self, nums):
        ans=[]
        for i in nums:
            i*=i
            ans.append(i)
        ans.sort()
        return ans    