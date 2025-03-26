# Creating the node
class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Creating the doubly linked list
class doublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    """Adding elements to Doubly LL"""
    # Adding to the beginning
    def insertBegin(self, data):
        newNode = node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode  # Update tail when inserting the first node
        self.head = newNode
    #adding to the end
    def insertEnd(self,data):
        if self.head is None:
            print("Empty dll - inserting in beginning")
            self.insertBegin(data)
            return
        newNode = node(data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
    #adding at a position
    def insertPos(self,data,pos):
        if pos == 0:
            self.insertBegin(data)
            return
        temp=self.head
        i=0
        while temp is not None and i<pos-1:
            temp=temp.next
            i+=1
        if temp is None:
            print("Out of range")
            return
        newNode = node(data)
        newNode.next = temp.next
        newNode.prev = temp
        if temp.next is None:
            self.tail = newNode
        else:
            temp.next.prev = newNode
        temp.next=newNode

    """Deletion of nodes in doubly linked lists"""
    #delete starting node:
    def delBegin(self):
        if self.head is None:
            print("Empty DLL, cant delete nothing")
            return
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = self.tail = None
            print("Deleted last node of the DLL")
            return
        self.head.prev = None

    #delete last node:
    def delEnd(self):
        if self.head is None:
            print("Empty Dll, cant delete nothing")
            return
        if self.tail.prev is None:
            print("Deleted last node of the DLL")
            self.head=self.tail=None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    #delete at a position:
    def delPos(self,pos):
        if self.head is None:
            print("Empty Dll, cant delete nothing")
            return
        if pos ==0:
            self.delBegin()
            return
        i=0
        temp = self.head
        while temp is not None and i<pos-1:
            temp=temp.next
            i+=1
        # Case 2: If position is out of bounds
        if temp is None or temp.next is None:
            print("Out of bound")
            return

        # Case 3: Deleting the last node (update tail)
        if temp.next.next is None:
            temp.next = None
            self.tail = temp
            return
        # Case 4: Deleting a node in the middle
        temp.next = temp.next.next
        if temp.next is not None:  # Check to prevent NoneType error
            temp.next.prev = temp


    #Reverse the doubly linked list using 3 pointers - prev, cur, next
    def revDllw3(self):
        if self.head is None:
            print("Empty DLL, cant reverse nothing")
            return
        prev = None
        cur = self.head
        next = self.head
        while next is not None:
            next = cur.next
            cur.next=prev
            cur.prev = next
            prev = cur
            cur=next
        temp =self.head
        self.head=self.tail
        self.tail=temp

    def revDll(self):
        if self.head is None:
            print("Empty DLL, cant reverse nothing")
            return
        cur = self.head
        next= self.head
        while next is not None:
            next = cur.next
            cur.next = cur.prev
            cur.prev = next
            cur=next
        cur = self.head
        self.head = self.tail
        self.tail = cur






    def print(self):
        if self.head is None:
            print("Empty DLL")
            return

        print("None <--> ",end="")
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <--> ")
            temp=temp.next
        print("None")

        if self.tail is not None:
            print("Tail = ", self.tail.data,"\n")
        else:
            print("Tail is none")

"""Implementation"""
dll = doublyLL()
dll.print()

dll.insertEnd(9)
dll.print()

dll.insertBegin(1)
dll.print()
dll.insertEnd(10)

dll.print()
dll.insertPos(0,0)
dll.print()

dll.insertPos(2,3)
dll.print()

dll.insertPos(1,100)
dll.print()

dll.delBegin()
dll.print()

dll.delEnd()
dll.print()

dll.delPos(1)
dll.print()

dll.delPos(1)
dll.print()

dll.delPos(1)
dll.print()

print("Before reversing:")
dll.insertBegin(6)
dll.insertBegin(12)
dll.insertBegin(9)
dll.print()

print("Reversed DLL:")
dll.revDllw3()
dll.print()

print("Reverse DLL w/ 2 ptrs:")
dll.revDll()
dll.print()











