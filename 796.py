#ROTATE STRING

class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        new=s
        for i in range(len(s)):
            if goal==new:    
                return True
            new=new[1:]+new[0]
        return False        