#THIS QUESTION 217 IN LEETCODE
#IN THIS QUESTION I LEARNT ABOUT USING AN EMPTY SET

class Solution(object):
    def containsDuplicate(self, nums):
        check=set()
        for no in nums:
            if no not in check:
                check.add(no)
            else:
                return True
        return False  