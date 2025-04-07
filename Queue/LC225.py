class MyStack:

    def __init__(self):
        self.q1=[]


    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1)==0 :
            print("Empty")
            return
        top=self.q1[-1]
        z=self.q1.pop()
        return z


    def top(self) -> int:
        if len(self.q1)>0:
            return self.q1[-1]
        else:
            print("Empty")
            return

    def empty(self) -> bool:
        if len(self.q1)==0 :
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()