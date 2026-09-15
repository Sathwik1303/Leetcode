#LINKED LIST CYCLE
'''
I FIRST SOLVED THIS QUESTION THROUGH MY APPROACH BUT THAT CODE FACED SOME 
EDGE CASES SO AGAIN I GOOGLE IT AND THEN UNDERSTOOD THE ANSWER.
'''

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False