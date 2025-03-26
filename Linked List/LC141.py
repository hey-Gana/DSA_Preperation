# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next is not None:
            slow = slow.next #goes one step
            fast = fast.next.next #Skipping 2 steps
            if slow is fast: #If it loops, both slow and fast pointers eventually meet
                print("Loop")
                return True
        return False
