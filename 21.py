#MERGING TWO LINKED LISTS
#ACTUALLY I GOT AN IDEA TO SOLVE THIS QUESTION BUT IT WAS NOT PERFECT
#SO THEN I SAW A TUTORIAL FOR THIS QUESTION AND LEARNT IT AND THEN MAKE THIS CODE RUN

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        header=dummy

        while list1 and list2:
            if list1.val<list2.val:
                header.next=list1
                list1=list1.next
            else:
                header.next=list2
                list2=list2.next
            header=header.next    
        header.next = list1 if list1 else list2

        return dummy.next                    

       