# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #No need of 2 pointers to head - ptr and cur_node; can work with just one pointer
        cur_node = head
        ptr = cur_node
        while ptr and ptr.next is not None:
            if ptr.val == ptr.next.val:
                #print("Duplicate")
                #Delete the node
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next


        #printing final answer
        # while cur_node is not None:
        #     print(cur_node.val)
        #     cur_node = cur_node.next

        return cur_node
