#VALID PARENTHESIS

class Solution(object):
    def isValid(self, s):
        pairs = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for i in s:
            if i in pairs:
                if not stack or stack[-1]!=pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0                

        