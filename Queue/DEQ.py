#Double Ended Queue
#A special type of queue which can have enqueue() and dequeue() from both ends of a queue.
#Application: Undo-Redo operations ; Multi-processor scheduling
from queue
def countStudents( students: list[int], sandwiches: list[int]) -> int:
    ans=0
    for i in range(len(sandwiches)):
        c=0
        while c<len(students) :
            c+=1
            q=students.pop()
            print(("Stu:",q))
            r=sandwiches.pop()
            print(("San:",r))
            if q!=r:
                print("chk")
                students.append(q)
                sandwiches.append(r)
            else:
                ans+=1
                print("C:",c)
                break
    print("A:",ans)
    return ans
stu = [1,1,1,0,0,1]
san=queue
san.put()


print(countStudents(stu,san))