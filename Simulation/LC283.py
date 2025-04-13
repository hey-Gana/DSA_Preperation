class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==0 and nums[j]!=0 and i!=j:
                    t=nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
        print(nums)