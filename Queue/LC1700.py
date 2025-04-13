#Interesting problem: Simulations
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rs=cs=0
        for i in students:
            if i ==0:
                rs+=1
            else:
                cs+=1
        for j in sandwiches:
            if j==0:
                if rs==0:
                    break
                else:
                    rs-=1
            else:
                if cs==0:
                    break
                else:
                    cs-=1

        return cs+rs
