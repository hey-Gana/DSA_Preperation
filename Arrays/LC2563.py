class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        count=0
        i=0
        j=len(nums)-1

        while(i<j):
            if nums[i]+nums[j]<=upper:
                count+=j-i
                i+=1
            else:
                j-=1

        i=0
        j=len(nums)-1
        countb=0
        while(i<j):
            if nums[i]+nums[j]<lower:
                countb+=j-i
                i+=1
            else:
                j-=1
        return count-countb