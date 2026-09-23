#SORT COLORS

class Solution(object):
    def sortColors(self, nums):
        zero=0
        one=0
        two=0
        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1
        nums[:]=[0]*zero + [1]*one + [2]*two 
        return nums

        