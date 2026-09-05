#THIS IS #643 QUESTION IN LEETCODE
#I SOLVED THIS QUESTION JUST AFTER LEARNING ABOUT SLIDING WINDOW WITHOUT USING HINTS

class Solution:
    def findMaxAverage(self,nums,k):
        currentsum=sum(nums[0:k])
        bestsum=currentsum
        for i in range(k,len(nums)):
            left=nums[i-k]
            right=nums[i]

            currentsum=currentsum+right-left

            if currentsum>bestsum:
                bestsum=currentsum

        return bestsum/k