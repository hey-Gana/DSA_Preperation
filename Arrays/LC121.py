class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #val=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff = prices[j]-prices[i]
        #         if diff>val:
        #             val=diff
        # return val

        p=0 #profit
        c=prices[0]#cheapest price
        for i in range(len(prices)):
            if prices[i]<c:
                c=prices[i]
            else:
                if p< prices[i]-c:
                    p=prices[i]-c
        return p
