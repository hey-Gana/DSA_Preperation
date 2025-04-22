class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums)==1 :
            return nums[0]
        else:
            chk=0
            nums.sort()
            print(nums)
            i=0
            while(i<len(nums)-1):
                print("i:",i)
                print("comparing:",nums[i],nums[i+1])
                if nums[i]==nums[i+1]:
                    print(nums[i],nums[i+1])
                    i+=2
                    print("u:",i)
                else:
                    chk=nums[i]
                    print("c:",chk)
                    i+=1
                    print("odd:",i)
                    return chk
            return(nums[len(nums)-1])


