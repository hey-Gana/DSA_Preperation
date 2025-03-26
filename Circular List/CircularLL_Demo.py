#creating a node
class Node:
    def __init__(self,data):
        self.head = None
        self.data = data

class circularLL:
    def __init__(self):
        self.tail = None

    """Insertion"""
    #instering in the beginning
    def insertBegin(self,data):
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            self.tail.next = newNode
            return
        newNode.next = self.tail.next
        self.tail.next = newNode

    #inserting at a position:
    def insertPos(self,data,pos):
        l = self.length()
        if pos<0 or pos>l:
            print("Wrong input of position")
            return
        if pos == 1:
            self.insertBegin(data)
            return
        elif pos == l:
            self.insertEnd(data)
            return
        newNode = Node(data)
        i=1
        temp = self.tail.next
        while i < pos-1:
            temp=temp.next
            i+=1
        newNode.next = temp.next
        temp.next = newNode


    #inserting in the end:
    def insertEnd(self,data):
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            self.tail.next = newNode
            return
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = newNode

    """Deletion in Circular LL"""
    #Deleting from beginning
    def delBegin(self):
        if self.tail is None:
            print("Cant delete nothing, Empty CLL")
            return
        temp = self.tail.next
        if temp is self.tail:
            print("Deleted Last Node in CLL")
            self.tail = None
            return
        self.tail.next = temp.next

    #Deleting from end
    def delEnd(self):
        if self.tail is None:
            print("Cant delete nothing, Empty CLL")
            return
        temp = self.tail.next
        if temp is self.tail:
            print("Deleted Last Node in CLL")
            self.tail = None
            return
        while temp.next is not self.tail:
            temp=temp.next
        temp.next = self.tail.next
        self.tail=temp

    #deleting from a position:
    def delPos(self,pos):
        l=self.length()
        if pos<0 or pos>l:
            print("Out of bound")
        if pos == 1:
            self.delBegin()
            return
        elif pos == l:
            self.delEnd()
            return
        temp = self.tail.next
        i=1
        while i<pos-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next


    def length(self)->int:
        if self.tail is None:
            print("Empty CLL")
            return
        l=0
        temp = self.tail.next
        while True:
            l+=1
            temp=temp.next
            if temp is self.tail.next:
                break
        print("Length: ", l)
        return l


    def print(self):
        if self.tail is None:
            print("Cll is empty")
            return
        temp = self.tail.next
        print("Tail <-> ", end="")
        while True:
            print(temp.data, end=" <-> ")
            temp=temp.next
            if temp is self.tail.next:
                break
        print("Head")
        print("Tail value: " , self.tail.data)



cll = circularLL()
cll.print()
cll.insertBegin(3)
cll.insertBegin(2)
cll.insertBegin(1)
cll.insertEnd(4)
cll.insertEnd(5)
cll.print()
cll.length()
cll.insertPos(10,3)
cll.print()
cll.length()

cll.delBegin()
cll.print()
cll.length()

cll.delEnd()
cll.print()
cll.length()

print("Del Pos")
cll.delPos(3)
cll.print()
cll.length()
