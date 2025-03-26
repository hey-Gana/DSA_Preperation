class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        flag=0
        c = ""
        for i in s:
            if i=="(":
                flag+=1
                if flag>1:
                    c+=i
            else:
                flag-=1
                if flag>0:
                    c+=i
        return c



