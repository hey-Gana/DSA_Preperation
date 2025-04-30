class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count=0
        for i in range(len(nums)):
            count_terms=0
            while(nums[i]!=0):
                rem=nums[i]%10
                count_terms+=1
                nums[i]=int(nums[i]/10)
                #print(rem,count_terms,nums[i])
            if count_terms%2==0:
                even_count+=1

        return(even_count)