# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        cur_node = head
        count =0
        sum = 0
        while cur_node is not None:
            count+=1
            cur_node = cur_node.next
        #print(count)
        temp_node = head
        i=1
        while temp_node is not None and i<=count:
            #print("temp:",temp_node.val)
            #j=pow(2,count-i)
            #print("Pow:",j)
            sum+=temp_node.val*pow(2,count-i)
            i+=1
            temp_node = temp_node.next
            #print(sum)
        print(sum)
        return sum

        