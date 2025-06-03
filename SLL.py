#singly linked list using python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, data):
        newNode = Node(data)  #makes a new node for the data
        if self.head is None: # if list is empty new node becomes the head
            self.head = newNode 
            
        else: # if not empty, new node's next node is the head and becomes the new head
            newNode.next = self.head
            self.head = newNode
            
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        currentNode = self.head
        while (currentNode != None and position+1 != index): # loop stops when position is found
            position +=1
            currentNode = currentNode.next
            
        if currentNode != None:
            newNode = Node(data) #makes new node for data
            newNode.next = currentNode.next #connects newNode to the next node of current
            currentNode.next = newNode #connects current node to the new Node
        else:
            print("index not found")
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.insertAtBegin(data)
            return
        
        
        currentNode = self.head
        while (currentNode.next): #breaks when currentNode.next is None
            currentNode = currentNode.next        
            
        currentNode.next  = newNode
        
    def updateNode(self, data, index):
        currentNode = self.head
        position = 0
        
        if position == index:
            currentNode.data = data
        else:
            while (currentNode != None and position != index):
                position += 1
                currentNode = currentNode.next
                
            if currentNode != None:
                currentNode.data = data
                
            else:
                print("index not present")
        
    def removeFirst(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        
    def removeEnd(self):
        if self.head is None:
            return
               
        currentNode = self.head
        while (currentNode.next != None and currentNode.next.next != None): #breaks when currentNode is 2nd to the last
            currentNode = currentNode.next        
            
        currentNode.next  = None
        
    def removeAtIndex(self, index):
        if self.head is None:
            return
        
        currentNode = self.head
        position = 0 
        
        if index == 0:
            self.removeFirst()
        
        else:
            while(currentNode != None and position + 1 != index):
                position +=1
        
        if currentNode != None:
            currentNode.next = currentNode.next.next
        else:
            print("index not present")       
        
    def printList(self):
        currentNode = self.head
        
        while currentNode: #loops until current node is None
            print(currentNode.data, end= "->")
            currentNode = currentNode.next
        print ("None")   
            
llist = LinkedList()

llist.insertAtBegin(1)
llist.insertAtIndex(2,1)
llist.insertAtIndex(3,1)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(6)

llist.updateNode(2,1)
llist.updateNode(3,2)

llist.removeFirst()
llist.removeAtIndex(2)
llist.removeEnd()

llist.printList()
        