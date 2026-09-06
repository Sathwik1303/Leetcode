#THIS IS #167 QUESTION IN LEETCODE 
#I SOLVED THIS QUESTION WITHOUT USING ANY HINTS
#I UNDERSTOOD THAT READING THE QUESTION PROPERLY IS VERY MUCH IMPORTANT

class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1

