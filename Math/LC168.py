class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=[]
        n=columnNumber

        while(n>0):
            rem=n%26
            n=int((n-rem)/(26))
            if rem==0:
                ans.append("Z")
                n-=1
            else:
                ans.append(chr(rem+64))
            print(n)
        #print(reversed(ans))
        print(ans.reverse())
        return "".join(ans)





        # while(columnNumber>0):
        #     rem=columnNumber%26+64
        #     print(rem-64)
        #     if rem==64:
        #         ans.append("Z")
        #         break
        #     else:
        #         ans.append(chr(rem))
        #     columnNumber=int(columnNumber/26)

        #     print("Q:",columnNumber)
        # print(ans)
       