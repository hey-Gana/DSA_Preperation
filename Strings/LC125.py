class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=s.lower().replace(" ","")
        l=re.sub(r'[^a-zA-Z0-9]', '', l)
        j=0
        i=0
        print(l)
        k=len(l)
        print(k)
        if k%2==0:
            i=int(k/2-1)
            j=int(k/2)
        else:
            i=int(k/2)
            j=int(k/2)
        print(i,j)

        while(i>=0 and j<k):
            if (l[int(i)] ==l[int(j)]):
                i-=1
                j+=1
                continue
            else:
                return False
        return True