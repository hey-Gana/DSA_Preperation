# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        t2 = head
        s=[]
        while temp is not None: #Pushing all elements into stack
            s.append(temp)
            temp=temp.next
        c=0
        k=t2
        l=len(s)
        # print(s)
        while(c!=l-1):
            if c%2==0:
                temp=t2.next
                t2.next=s.pop()
                t2=t2.next
                c+=1
            else:
                t2.next=temp
                t2=t2.next
                c+=1

        t2.next = None
        while k is not None:
            print(k.val)
            k=k.next

# *Interesting manipulation of linked lists.




