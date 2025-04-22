class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        for i in range(n):
            sum=a+b
            a=b
            b=sum
        #print(a,b,sum)
        return sum