class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        #print(ans)
        return ans