class Solution:
    def reverseString(self, s: List[str]) -> None:
        j=len(s)-1
        i=0
        while(i<=int(len(s)/2) and j>=int(len(s)/2)):
            t=s[i]
            s[i]=s[j]
            s[j]=t
            i+=1
            j-=1
        print(s)
