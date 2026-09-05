#THIS IS #242 QUESTION IN LEETCODE
#FROM THIS QUESTION I LEARNT ABOUT SORTED FUNCTION

class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s)==sorted(t):
            return True
        return False   
        