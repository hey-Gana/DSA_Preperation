class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        ans=0
        for i in range(len(tokens)):
            #print(tokens[i])
            if tokens[i] not in ["+","-","/","*"]:
                s.append(tokens[i])
            else:
                if tokens[i]=="+":
                    i=int(s.pop())
                    j=int(s.pop())
                    s.append(i+j)
                    #print(s)
                elif tokens[i]=="-":
                    i=int(s.pop())
                    j=int(s.pop())
                    s.append(j-i)
                    #print(s)
                elif tokens[i]=="*":
                    i=int(s.pop())
                    j=int(s.pop())
                    s.append(i*j)
                    #print(s)
                elif tokens[i]=="/":
                    i=int(s.pop())
                    j=int(s.pop())
                    s.append(j/i)
                    #print(s)
        #print(s)
        return int(s[-1])