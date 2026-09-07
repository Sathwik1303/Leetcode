#THIS IS #283 QUESTION IN LEETCODE.
#I GOT TO KNOW THAT I AM NOT READING THE QUESTION PROPERLY BECAUSE
#I USED SORT FUNCTION BEFORE WHICH WAS NOT NEEDED.

class Solution(object):
    def moveZeroes(self, nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        return nums