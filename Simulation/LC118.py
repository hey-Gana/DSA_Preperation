from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []

        for i in range(numRows):
            a.append([0] * (i + 1))  # Initialize row with 0s

            for j in range(i + 1):  # j should go from 0 to i
                if j == 0 or j == i:
                    a[i][j] = 1
                else:
                    a[i][j] = a[i-1][j-1] + a[i-1][j]

        return a
