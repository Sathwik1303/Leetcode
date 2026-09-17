#LENGTH OF LAST WORD
'''
HERE ALSO I WROTE THE ENTIRE PROGRAM ON MY OWN AND AGAIN I GOT STRUCK AT 
THE RETURN STATEMENT SO I GOOGLED IT AND LEARNT ABOUT NEW FUNCTION..
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        index=0
        s = s.rstrip()
        for i in range(len(s)):
            if (s[i]==" ") and i+1<len(s) and s[i+1]!=" ":
                index=i+1
        word=s[index:]       
        return len(word)

        