class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        diff=0
        ans=1
        i=1

        while(i<=x/2):
            diff=x-i*i
            if diff==0:
                return i
            elif diff<0:
                break
            else:
                ans=i
                i+=1

        return ans


        # while(mid>0):
        #     diff=x-mid*mid
        #     if diff>0:
        #         mid=mid/2
        #     elif diff==0:
        #         return mid
        #     else:
        #         mid=mid+mid/2
        # return mid

        #print(mid)
        # if x>0:
        #     if x==1:
        #         return 1
        #     while(mid>2):

        #         k=i*i
        #         print(k)
        #         diff = x-k
        #         print(diff)
        #         if diff == 0:
        #             return i
        #         elif diff>0:
        #             ans=i
        #         else:
        #             break
        # else:
        #     return 0


