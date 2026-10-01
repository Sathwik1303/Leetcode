#FIND ALL DUPLICATES IN AN ARRAY

class Solution(object):
    def findDuplicates(self, nums):
        seen=set()
        dup=[]
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                dup.append(i)

        dup.sort()
        return dup