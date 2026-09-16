#PALINDROME LINKED LIST
'''
FIRST I DID THIS QUESTION USING CLASS METHOD IN STACK SO I GOT EDGE CASE ERROR 
WHILE SUBMITTING SO AGAIN I SHIFTED TO LIST METHOD.
'''

class Solution(object):
    def isPalindrome(self, head):
        current=head
        if current is None:
            return True
        value=[]
        while current:
            value.append(current.val)
            current=current.next
        return value==value[::-1]