#THIS IS #189 QUESTION IN LEETCODE
#WHILE SUBMITTING THE CODE I FACED AN ERROR WHICH WAS LIKE WHAT IF K>LEN(NUMS)
#I DID NOT UNDERSTAND SO I GOOGLED IT THEN I GOT TO KNOW I WAS SUPPOSED TO USE %

class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        rotation=nums[len(nums)-k:len(nums)]
        leftover=nums[0:len(nums)-k]

        nums[:]=rotation+leftover
        
        