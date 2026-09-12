#REVERSING A LINKED LIST
'''

I AM ABLE TO SOLVE THE PROBLEM BUT I AM UNABLE TO WRITE THE SYNTAX PROPERLY
SO I NEED TO UNDERSTAND THE SYNTAX MORE CLEARLY..

'''

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None

        prev=None
        current=head

        while current is not None:
            new=current.next
            current.next=prev
            prev=current
            current=new

        return prev   