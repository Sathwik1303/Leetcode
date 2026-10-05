#FIND MINIMUM IN MINIMUM SORTED ARRAY

class Solution(object):
    def findMin(self, nums):
        current=nums[0]
        for i in nums[1:]:
            if current>i:
                current=i
        return current        


        