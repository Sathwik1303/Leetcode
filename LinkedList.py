#IN THIS I PRACTICED HOW TO MAKE A LINKED LIST , APPEND A LINKED LIST, DISPLAY
#I FACED MANY PROBLEMS WHILE LEARNING THIS BECAUSE
#I COULD NOT UNDERSTAND THE SYNTAX DIRECTLY BY WATCHING..

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def printing(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

l = Linkedlist()
l.append(10)
l.printing()   # 10->None
l.append(20)
l.printing()   # 10->20->None