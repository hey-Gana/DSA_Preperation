class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum=0
        for op in operations:
            print(stack)
            if op == "+":
                print("+")
                if len(stack)>=2:
                    q=stack[-1]+stack[-2]
                    stack.append(q)
            elif op == "D":
                c=2*stack[-1]
                print(c)
                stack.append(c)
                print("D")
            elif op  == "C":
                stack.pop()
                print("C")
            else:
                stack.append(int(op))
                print("Integer")
        print(stack)
        for i in range(len(stack)):
            sum+=stack.pop()
        return sum


