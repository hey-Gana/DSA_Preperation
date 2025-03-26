"""Stack has 2 types of implementations - Array & LinkedLists """

#LinkedLists Implementation
class Node:
    def __init__(self,x):
        self.value=x
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        nnode = Node(x)
        nnode.next = self.head
        self.head= nnode

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        print(f"Element removed {self.head.value}")
        self.head=self.head.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"Value : {temp.value}")
            temp=temp.next
print("Linked List Implementation")
s=stack()
s.push(5)
s.push(2)
s.push(4)
s.push(8)
s.push(9)
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()


#Array Implementation
class arrstack:
    def __init__(self, limit):
        self.limit = limit
        self.top = -1
        self.a = [None]*limit #creates an empty array with size inputed as limit
        print(f"Created stack of size: {len(self.a)}")

    def push(self, x):
        if self.top >= self.limit-1:
            print("Stack Overflow")
            print(f"Top : {self.top}")
            return
        self.top+=1
        self.a[self.top]=x
        print(f"Inputed element {x} in position: {self.top}")

    def pop(self):
        if self.top <0:
            print("Stack is empty")
            print(f"Top : {self.top}")
            return
        print(f"popping element: {self.a[self.top]}")
        self.top-=1

    def peek(self):
        if self.top<0:
            print("Stack is empty")
            print(f"Top : {self.top}")
            return
        print(f"Top element: {self.a[self.top]}")
    def display(self):
        if self.top<0:
            print("Stack is empty")
            print(f"Top : {self.top}")
            return
        for i in range(self.limit-1,-1,-1):
            print(f"value: {self.a[i]}")

print("Array Implementation")
s=arrstack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.peek()
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()





