# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        #print(type(list1))
        ans = ListNode() #initializing empty node ; acts as head
        ptr = ans #dummy pointer
        while list1 and list2 is not None:
            if list2.val >= list1.val:
                ptr.next=list1
                list1 = list1.next
            else:
                ptr.next=list2
                list2 = list2.next
            ptr=ptr.next
        #appending leftover nodes to pointer
        if list1 is None:
            ptr.next = list2
        elif list2 is None:
            ptr.next = list1


        # while ans.next is not None:
        #     ans=ans.next
        #     print(ans.val)
        return ans.next   