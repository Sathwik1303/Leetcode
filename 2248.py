#INTERSECTION OF MULTIPLE ARRAYS

class Solution(object):
    def intersection(self, nums):
        count={}
        for i in nums:
            for j in i:
                count[j]=count.get(j,0)+1
        result=[]        
        for key,val in count.items():
            if val == len(nums):
                result.append(key)
        result.sort()
        return result

