class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i =="#" and len(stack1)>0:
                stack1.pop()
            elif i!="#":
                stack1.append(i)

        for j in t:
            if j =="#" and len(stack2)>0:
                stack2.pop()
            elif j!="#":
                stack2.append(j)

        print(stack1)
        print(stack2)
        if stack1 == stack2:
            return True

        return False