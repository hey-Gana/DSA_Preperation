class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[] #temp


    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        k=self.s2.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return k

    def peek(self) -> int:
        if len(self.s1)==0:
            return
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        k=self.s2[-1]
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return k




    def empty(self) -> bool:
        if len(self.s1)==0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()