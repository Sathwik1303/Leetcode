#REMOVING DUPLICATES FROM SORTED LIST
'''
I SOLVED THIS QUESTION AND SUBMITTED THIS CODE BY AFTER THEN IT GAVE AN
EDGE CASE ERROR SO I GOOGLED IT AND THEN AGAIN SUBMITTED.
'''

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        extra = ListNode(0)
        extra.next = head
        prev = extra
        while current:
            if prev != extra and current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return extra.next