class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        ans=[]
        for i in range(low,high+1):
            sum1=0
            sum2=0
            a=[]
            count=0
            k=i
            while i !=0 :
                a.append(int(i%10))
                count+=1
                i=int(i/10)
            #print(a)
            if count%2!=0:
                #print("ODD")
                continue
            else:
                p1=int(len(a)/2)
                p2=p1-1
                while(p1<=len(a)-1 and p2>=0):
                    sum1+=a[p1]
                    sum2+=a[p2]
                    p1+=1
                    p2-=1
                if sum1==sum2:
                    ans.append(k)

        print(ans)
        return len(ans)
