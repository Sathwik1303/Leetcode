#THIS IS #28 QUESTION IN LEETCODE
#I SOLVED THIS CODE UPTO 95 PERCENT BUT I USED SEPARATE VARIABLE WHICH CAUSED
#SOME PROBLEM WHILE SUBMITING SO THEN I USED I WHICH IS IN LOOP..

class Solution(object):
    def strStr(self, haystack, needle):
        p=len(needle)
        for i in range(0,len(haystack)-p+1):
            if haystack[i:p+i]==needle:
                return i
        return -1 