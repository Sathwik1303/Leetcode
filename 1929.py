#1929 CONCATENATION OF ARRAYS
#THIS THE CODE THAT I SUBMITTED IN LEETCODE

class Solution(object):
    def getConcatenation(self, nums):
        ans=nums+nums
        return ans
    
#THIS IS THE CODE THAT I RAN LOCALLY

class Solution:
    def getConcatenation(self, nums):
        ans=nums+nums
        return ans

nums=[]
n=int(input("Enter the length of array:"))

for i in range(n):
    value=int(input(("Enter value:")))
    nums.append(value)

sol=Solution()
ans=sol.getConcatenation(nums)
print(ans)
