class Solution:
    def minLength(self, s: str) -> int:
        a=[""]

        for i in s:
            if (a[-1]=="C" and i=="D") or (a[-1]=="A" and i =="B"):
                a.pop()
            else:
                a.append(i)

        return len(a)-1
