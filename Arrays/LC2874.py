class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        l=len(nums)
        ans=0
        pre=nums[0]
        maxdif=0
        if l<2:
            return 0
        elif l==3:
            if (nums[0] - nums[1]) * nums[2]<0:
                return 0
            else:
                return (nums[0] - nums[1]) * nums[2]
        else:
            for j in range(1,l-1):
                pre = max(pre, nums[j-1])
                maxdif = max(maxdif, pre-nums[j])
                ans = max(ans, maxdif*nums[j+1])
        print(ans)
        return ans
