#DELETE THE MIDDLE NODE OF A LINKED LIST
'''
I SOLVED 95 PERCENT OF THE QUESTION BUT GOT STRUCK WHEN THE COUNT IS 1
SO THIS SMALL PART TOOK TIME.
'''

class Solution(object):
    def deleteMiddle(self, head):
        count=0
        current=head
        while current:
            current=current.next
            count+=1
        if (count-1)%2==0:
            delete=(count-1)/2
        else:
            delete=(count)/2
        prev=head
        n=0

        if (count ==1):
            return None

        while (n<(delete-1)):
            prev=prev.next
            n+=1
        prev.next=prev.next.next

        return head 