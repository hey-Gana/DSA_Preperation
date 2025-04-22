class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        for i in range(len(arr)-2):
            for j in range(1,len(arr)-1,1):
                for k in range(2,len(arr),1):
                    #print(i,j,k)
                    if(j>i and k>j):
                        c1=abs(arr[i]-arr[j])
                        c2=abs(arr[j]-arr[k])
                        c3=abs(arr[k]-arr[i])
                        if(c1<=a and c2<=b and c3<=c):
                            count+=1
                            #print(i,j,k)
                            #print(arr[i],arr[j],arr[k])
                        else:
                            continue
        print(count)
        return count
