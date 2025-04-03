class Solution:
    def maxDepth(self, s: str) -> int:
        flag=0
        stack=[]
        for i in s:
            if i == '(':
                flag+=1
                stack.append(flag)
            elif i ==  ')':
                flag-=1
            else:
                continue
        print(stack)
        max=0
        for i in range(0,len(stack)):
            k=stack.pop()
            if max<k:
                max=k

        return max