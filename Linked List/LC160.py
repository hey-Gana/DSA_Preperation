# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        #both the pointers traverse same distance when traversing both linked lists

        pa=headA
        pb=headB
        while pa is not pb:
            if pa is not None:
                pa = pa.next
            else:
                pa =headB

            if pb is not None:
                pb = pb.next
            else:
                pb=headA

        return pa



