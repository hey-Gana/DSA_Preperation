class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split("/")
        a=[]
        # a.append("/")
        print(s)
        for i in range(len(s)):
            if s[i]=='' or s[i]==".":
                continue
            elif s[i]=="..":
                if len(a)>0:
                    a.pop()
            else:
                a.append(s[i])

        print(a)
        print(len(a))

        return "/"+"/".join(a)





