class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        if rowIndex==0:
            a.append(1)
            return a


        for i in range(rowIndex+1):
            row=[1]*(i+1)
            a.append(row)
            for j in range(i):
                if i==j or j==0:
                    a[i][j]=1
                else:
                    a[i][j]=a[i-1][j-1]+a[i-1][j]

        return (a[rowIndex])
