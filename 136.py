#SINGLE NUMBER
'''
I COULD SOLVE THE ENTIRE QUESTION BUT I WAS UNABLE TO WRITE THE SYNTAX OF 
RETURN STATEMENT SO I GOOGLED IT.
'''

class Solution(object):
    def singleNumber(self, nums):
        seen=set()
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)     
        return list(seen)[0]
                