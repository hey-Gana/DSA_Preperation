def checkParanthesis(s):
    stack = []
    ans = True
    for i in range(len(s)):
        if(s[i]=="(" or s[i]=="{" or s[i]=="["):
            stack.append(s[i])
        elif((s[i]==")" or s[i]=="}" or s[i]=="]") and (len(stack)>0)):
            c=stack.pop()
            if(s[i]==")" and c == "(") or (s[i]=="}" and c == "{")  or (s[i]=="]" and c == "[") :
                continue
            else:
                ans = False
        else:
            ans = False
    if len(stack)>0:
        ans=False
    return ans

s = "][)("
print(checkParanthesis(s))
