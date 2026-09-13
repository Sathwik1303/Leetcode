#MIDDLE OF THE LINKED LIST
'''
THIS IS THE FIRST QUESTION WHICH I SOLVED WHICH IS RELATED TO LINKED LIST.
'''

class Solution(object):
    def middleNode(self, head):
        count=0
        current=head
        while current:
            current=current.next
            count+=1
        middle=count//2
        link=head
        n=0
        while n<middle :
            link=link.next
            n+=1 
        return link    