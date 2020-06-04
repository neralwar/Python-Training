class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def _init_(self):
        self.head = None

    def printList(self): 
        temp = self.head 
        lilist = []
        while (temp): 
            lilist.append(temp.data)
            temp = temp.next
            
        #print("=>".join(lilist))
        print("=>".join(lilist))

l = Linkedlist()
l.head = Node("Ashish")
second = Node("Neralwar")
third = Node("Ramesh")

l.head.next = second

second.next = third

l.printList()

#print("=>".join(l.head))








