class Solution:
    def clearDigits(self, s: str) -> str:
        k=[]
        for i in s:
            if i.isdigit():
                k.pop()
            else:
                k.append(i)
        return "".join(k)