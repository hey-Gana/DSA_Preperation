class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l=len(nums)
        if l<2:
            return 0
        elif l==3:
            if (nums[0] - nums[1]) * nums[2]<0:
                return 0
            else:
                return (nums[0] - nums[1]) * nums[2]
        else:
            c=nums[0]
            ans=0
            for j in range(1,l):
                if c<nums[j]:
                    c=nums[j]
                for k in range(j+1,l):
                    ans = max(ans, (c-nums[j])*nums[k])
            print(ans)
            return ans
