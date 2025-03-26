# Creating a structure for node
class node:
    def __init__(self, data):  # Constructor to initialize its value
        self.data = data
        self.next = None

# Creating LinkedList Class
class LinkedListL:
    def __init__(self):  # Constructor to initialize head
        self.head = None

    # Adding element to linked list
    # Adding to the beginning
    def insertBegin(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode
        # newNode.next = None

    # Adding at a specific position
    def insertPos(self, data, pos):
        if pos == 0:
            self.insertBegin(data)
            return

        cur_node = self.head
        i = 0
        while cur_node is not None and i + 1 != pos:
            cur_node = cur_node.next
            i += 1

        if cur_node is not None:
            newNode = node(data)
            newNode.next = cur_node.next
            cur_node.next = newNode
        else:
            print("Index not present")

    # Adding to the end
    def insertEnd(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            return
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = newNode

    # Updating element in linked list
    def updateNode(self, val, pos):
        cur_node = self.head
        i = 0
        while cur_node is not None and i != pos:
            cur_node = cur_node.next
            i += 1
        if cur_node is not None:
            cur_node.data = val
        else:
            print("Index not present")

    # Deleting the first element
    def delFirst(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # Deleting the last element
    def delLast(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None

    # Deleting at a specific position
    def delPos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.delFirst()
            return
        cur_node = self.head
        i = 0
        while cur_node.next is not None and i + 1 != pos:
            cur_node = cur_node.next
            i += 1
        if cur_node.next is not None:
            cur_node.next = cur_node.next.next
        else:
            print("Index not present")

    # Removing a node with a specific value
    def remData(self, val):
        cur_node = self.head
        if cur_node is not None and cur_node.data == val:
            self.delFirst()
            return
        while cur_node.next is not None:
            if cur_node.next.data == val:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next
        print("Value not found in linked list")

    # Finding the size of linked list
    def sizeofLL(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    # Printing linked list elements
    def printLL(self):
        cur_node = self.head
        if cur_node is None:
            print("List is empty")
            return
        while cur_node is not None:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    #Reversing a Linked List
    def revLL(self):
        prev_node = None
        cur_node = self.head
        next_node = self.head

        if cur_node is None:
            print("Empty linked list")
            return

        while next_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        self.head = prev_node

# Create an object for the class
llist = LinkedListL()

# Testing all functions
llist.insertBegin('a')
llist.insertBegin('b')
llist.insertEnd('q')
llist.insertEnd('d')
llist.insertPos('g', 2)

print("Linked List after insertions:")
llist.printLL()

print("Linked List after reversing:")
llist.revLL()
llist.printLL()

print("Size of Linked List:", llist.sizeofLL())

llist.remData('a')
print("Linked List after removing 'a':")
llist.printLL()

llist.delFirst()
print("Linked List after deleting first element:")
llist.printLL()

llist.delLast()
print("Linked List after deleting last element:")
llist.printLL()

llist.delPos(1)
print("Linked List after deleting position 1:")
llist.printLL()

llist.updateNode('z', 1)
llist.updateNode('k', 5)
print("Linked List after updates:")
llist.printLL()

print("Final Size of Linked List:", llist.sizeofLL())
