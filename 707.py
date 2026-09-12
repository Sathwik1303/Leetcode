#IN THIS I PRACTICED HOW TO CREATE A LINKED LIST 
# AND APPEND,DELETE,ETC OPERATION IN THIS LINKED LIST

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        # Initialize sentinel head and tail nodes
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        # Optimize by traversing from the closer side
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
                
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index,val):
        if index > self.size:
            return
        if index < 0:
            index = 0
            
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
            
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
            
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - 1 - index):
                succ = succ.prev
            pred = succ.prev.prev
            
        pred.next = succ
        succ.prev = pred
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
