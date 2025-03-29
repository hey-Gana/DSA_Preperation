# for i in range(97,123):
#     print(chr(i)) #small letters
#
# for j in range(65,91):
#     print(chr(j)) #Cap letters

s = "LeEeeTCode"
# for i in range(len(s)):
#     print(ord(s[i])) #ord() -> converts the character to its ASCII value

class Solution:
    def makeGood(self, s: str) -> str:
        l=len(s)
        if l==0 or l==1:
            return s
        else:
            stack=[]

            for i in range(0,l):
                if len(stack)==0:
                    print(s[i],"-emp")
                    stack.append(s[i])
                    continue
                else:
                    top = stack.pop()
                    print(top, "-TOP")
                    if (ord(top)-ord(s[i])) == 32 or (ord(s[i])-ord(top))==32:
                        print(top, s[i], "DEL")
                        continue
                    else:
                        print(top, s[i], "ADD")
                        stack.append(top)
                        stack.append(s[i])
            q=[]
            for i in range(0,len(stack)):
                q.append(stack.pop())
            q.reverse()
            print(q)
            return "".join(q)

