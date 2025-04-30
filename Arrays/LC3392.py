class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)-1):
            prev = nums[i-1]
            next=nums[i+1]
            #print("Prev, Next:", prev , "-", next)
            if nums[i]/2 == (prev+next):
                c+=1

        #print("ans:",c)
        return c