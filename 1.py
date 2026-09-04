#THIS IS THE #1 SUM IN LEECODE
#I SOLVED THIS QUESTION USING 2 POINTER METHOD
#I FACED A PROBLEM IN CASE 2 BUT AT LAST SOLVED IT

class Solution(object):
    def twoSum(self, nums, target):
        left=0
        right=len(nums)-1
        copyy=nums.copy()
        nums.sort()

        while left<right:
            sum=nums[left]+nums[right]
            if sum==target:
                idx1=copyy.index(nums[left])
                if nums[left]==nums[right]:
                    idx2=copyy.index(nums[right],idx1+1)
                else:
                    idx2=copyy.index(nums[right])
                return [idx1,idx2]        

            elif sum<target:
                left=left+1
            else:
                right=right-1