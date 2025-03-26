# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        #if empty
        if head is None:
            return
        #if it is repeating in the starting
        while head is not None and head.val == val:
            head=head.next #moving head forward

        #if it is repeating after the beginning, traverse and delete
        cur_node = head
        temp = None
        while cur_node is not None:
            if cur_node.val == val:
                temp.next = cur_node.next
            else:
                temp = cur_node
            cur_node=cur_node.next

        # while head is not None:
        #     print(head.val)
        #     head=head.next
        return head


