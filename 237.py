#DELETING A NODE FROM A LINKED LIST
'''
I SOLVED THIS ENTIRE QUESTION ON MY OWN..
'''

class Solution(object):
    def deleteNode(self, node):
        current=node
        
        current.val=current.next.val
        current.next=current.next.next