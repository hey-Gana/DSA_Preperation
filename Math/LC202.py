class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1 and n not in seen:
            seen.append(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
