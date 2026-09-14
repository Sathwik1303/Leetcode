#ROTATE LIST
'''
I COULD SOLVE 70 PERCENT OF THE PROBLEM BUT I COULDNT MAKE THE CODE 
EFFICIENT SO I TOOK THE HELP OF CLAUDE THEN I UNDERSTOOD THE LOGIC
AND AGAIN IMPLEMENTED THAT LOGIC.
'''

class Solution(object):
    def rotateRight(self, head, k):
        if (not head or not head.next or k==0):
            return head
        tail=head
        length=0
        while tail:
            tail=tail.next
            length+=1    
        k=k%length
        if k==0:
            return head
        for i in range(k):        
            current=head.next
            prev=head
            while current and current.next:
                current=current.next
                prev=prev.next
            prev.next=None
            current.next=head
            head=current    

        return head