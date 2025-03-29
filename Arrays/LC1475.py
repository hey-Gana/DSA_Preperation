class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        ans = []
        for i in range(0,len(prices)):
            j=i+1
            discount =0
            while(j<len(prices)):
                if(prices[j]<=prices[i]):
                    discount=prices[j]
                    print("Discount:",discount)
                    break
                else:
                    j=j+1
            print(prices[i]-discount)
            ans.append(prices[i]-discount)
        return ans