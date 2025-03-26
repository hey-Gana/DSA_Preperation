class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=""
        stack=[]
        for i in range(len(s)):
            if len(stack)>0:
                c=stack.pop()
                if c==s[i] and len(stack)>=-1:
                    continue
                else:
                    stack.append(c)
                    stack.append(s[i])

            else:
                stack.append(s[i])
        print(stack)

        while stack:
            a+=stack.pop()
        a=a[::-1]
        return a




