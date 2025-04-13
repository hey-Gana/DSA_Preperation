class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        k=len(s)
        i=len(s)-1 #size of cookies
        j=len(g)-1 #greed
        while(i>=0 and j>=0):
            print(i,j)
            if s[i]>=g[j]:
                s.pop()
                g.pop()
                print("POP")
                i-=1
            j-=1

        count = k-len(s)
        return count






