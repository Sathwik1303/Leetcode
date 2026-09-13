#REMOVING NTH NODE FROM THE END
'''
SO I SOLVED MORE THAN 70 PERCENT OF THE QUESTION BUT I WAS STRUCK AT THE 
CONNECTION OF NODES SO I KNOW THE LOGIC BUT COULDNT PUT IT IN THE FORM OF 
SYNTAX,I GOOGLED IT AND UNDERSTOOD THE REMAINING PROCESS.
'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        current=head

        while current:
            current=current.next
            count+=1

        handling=ListNode(0)
        handling.next=head
        prev=handling

        for i in range(count-n):
            prev=prev.next
        prev.next=prev.next.next
        
        return handling.next 