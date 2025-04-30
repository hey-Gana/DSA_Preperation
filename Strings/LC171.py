class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # print(chr(65))
        c=0
        k=len(columnTitle)
        ex_val=0
        for i in range(k-1,-1,-1):
            chr_val= ord(columnTitle[i])-64
            ex_val += (26**c) * chr_val
            c+=1
        return (ex_val)

