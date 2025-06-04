class Solution:
    def candy(self, ratings: List[int]) -> int:
        min=0
        c=[1]*len(ratings)
        #print("check",c)
        if len(ratings)<2:
            return 1
        elif len(ratings)==2:
            if ratings[0]!=ratings[1]:
                return 3
            else:
                return 2
        else:
            for i in range(len(ratings)-1):
                if ratings[i+1]>ratings[i]:
                    c[i+1]=c[i]+1
            print(c)
            for j in range(len(ratings)-1,0,-1):
                print(j)
                if ratings[j-1]>ratings[j]:
                    print("comparing - ", ratings[j],"- ", ratings[j-1])
                    temp=c[j-1]
                    k=c[j]+1
                    c[j-1]=max(temp,k)
            for i in range(len(ratings)):
                min+= c[i]

            return min



