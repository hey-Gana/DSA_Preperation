#Circular List Implimentation
class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class clq:
    def __init__(self):
        self.head =None
        self.tail = None

    def enq(self,n):
        newNode = node(n)
        if self.head is None:
            self.head=newNode
            self.tail=self.head
            self.tail.next = self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            newNode.next=self.head

    def deq(self):
        if self.head is None:
            print("Empty Node")
            return
        if self.head is self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head

    def display(self):
        if self.head is None:
            print("Empty Node")
            return
        temp = self.head
        while True:
            print(temp.val)
            temp = temp.next
            if temp == self.head:
                break


o4=clq()
o4.enq(1)
o4.enq(2)
o4.enq(3)
o4.enq(4)
o4.display()
o4.deq()
o4.deq()
o4.display()
o4.deq()
o4.deq()
o4.display()
o4.deq()




#Linked List Implimentation
class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LList:
    def __init__(self):
        self.head = None
        self.tail=None

    def enq(self,n):
        newNode = node(n)
        if self.head is None:
            self.head= newNode
            self.tail=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode

    def deq(self):
        if self.head is None:
            print("Empty Queue")
        else:
            self.head=self.head.next

    def display(self):
        if self.head is None:
            print("Empty Queue")
            return
        temp=self.head
        while temp is not None:
            print(temp.val)
            temp=temp.next

o3=LList()
o3.enq(1)
o3.enq(2)
o3.enq(3)
o3.enq(4)
o3.display()
o3.deq()
o3.display()
o3.enq(5)
o3.display()
o3.deq()
o3.deq()
o3.deq()
o3.deq()
o3.deq()
o3.deq()
o3.display()




#Array Implimentation using Circular Array structure(overcomes the drawback of using linear array structure)

class cQ:
    def __init__(self,size):
        self.s=size
        self.front=-1
        self.rear=-1
        self.a = [None]*size #Creates an empty array of the given size
        print(f"Created Queue with size: {self.s}")

    def enq(self, n):
        if (self.front+1)%2==self.rear:
            print("Queue is full")
            return
        if self.rear==-1 and self.front==-1:
            self.front+=1
            self.a[self.front]=n
            self.rear+=1
            print(f"Enqued in position: {self.rear}")
        else:
            self.rear=(self.rear+1)%self.s
            self.a[self.rear]=n
            print(f"Enqued in position: {self.rear}")

    def deq(self):
        if self.rear==-1 and self.front==-1:
            print("Queue Empty")
        elif self.front==self.rear:
            print(f"Element Dequed: {self.a[self.front]}")
            self.front=-1
            self.rear=-1
        else:
            print(f"Element Dequed from :{self.front}")
            self.front=(self.front+1)%self.s

    def display(self):
        if self.rear==-1 and self.front==-1:
            print("Queue Empty")
        else:
            i=self.front
            while True:
                print(self.a[i])
                if i==self.rear:
                    break
                i=(i+1)%self.s


o2 = cQ(5)
o2.enq(1)
o2.enq(2)
o2.deq()
o2.enq(3)
o2.enq(4)
o2.enq(5)
o2.display()
o2.deq()
o2.display()
o2.enq(4)
o2.enq(5)
o2.enq(4)
o2.enq(5)
o2.display()
o2.deq()
o2.display()
o2.deq()
o2.deq()
o2.deq()
o2.deq()
o2.deq()








#Array Implimentation using linear array structure
# Drawback of this is: After dequeue of last element of the size of array, no element can be inserted;
# since we have to maintain adding and removing elements with O(1) time.


class arrQ:
    def __init__(self,size):
        self.s=size
        self.front=-1
        self.rear=-1
        self.a = [None]*size #Creates an empty array of the given size
        print(f"Created Queue with size: {self.s}")

    def enq(self, n):
        if self.rear==self.s-1:
            print("Queue Overloaded")
        elif self.rear==-1 and self.front==-1:
            self.front+=1
            self.a[self.front]=n
            self.rear+=1
            print(f"Enqued in position: {self.rear}")
        else:
            self.rear+=1
            self.a[self.rear]=n
            print(f"Enqued in position: {self.rear}")

    def deq(self):
        if self.rear==-1 and self.front==-1:
            print("Queue Empty")
        elif self.front!=self.rear+1:
            print(f"Element Dequed: {self.a[self.front]}")
            self.front+=1
        else:
            print("Cannot Deque further")

    def display(self):
        if self.rear==-1 and self.front==-1:
            print("Queue Empty")
        else:
            for i in range(self.front,self.s):
                print(f"Element: {self.a[i]}")


o1=arrQ(5) #Creating Queue of size 5
o1.display()
o1.enq(1)
o1.enq(2)
o1.deq()
o1.deq()
o1.display()
o1.enq(3)
o1.display()
o1.enq(4)
o1.enq(5)
o1.enq(6)
o1.display()
o1.deq()
o1.deq()
o1.deq()
o1.deq()
o1.deq()
o1.deq()
o1.deq()
o1.enq(1)
o1.enq(2)





