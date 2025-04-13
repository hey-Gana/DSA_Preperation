class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        print("C: ",count)
        for i in range (len(tickets)):
            print("i,k: ",i,k)
            print("vals: ",tickets[i],tickets[k])
            if i<=k:
                count+=min(tickets[i],tickets[k])
            else:
                count+=min(tickets[i],tickets[k]-1)

        print("C: ",count)
        return count