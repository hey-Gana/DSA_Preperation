# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        cur_node = next_node = head
        prev_node = None
        head1 = None
        a=[]

        while cur_node is not None:
            a.append(cur_node.val)
            cur_node = cur_node.next

        # print("Array: ",a)
        j=len(a)-1
        for i in range(0,len(a)):
            if a[i] == a[j]:
                i+=1
                j-=1
            else:
                return False

        return True


        # #reversing the LL
        # while next_node is not None:
        #     #Creating a copy of the linked list
        #     newNode = ListNode(next_node.val)
        #     if head1 is None:
        #         head1 = newNode
        #     else:
        #         cnode = head1
        #         while(cnode.next is not None):
        #             cnode = cnode.next
        #         cnode.next = newNode
        #     #Reversing the linked list
        #     next_node = next_node.next
        #     cur_node.next = prev_node
        #     prev_node = cur_node
        #     cur_node = next_node
        # head = prev_node



        # head1 = None
        # #Copying the LL:
        # while(next_node is not None):
        #     newNode = ListNode(next_node.val)
        #     if head1 is None:
        #         head1 = newNode

        #     else:
        #         cnode = head1
        #         while(cnode.next is not None):
        #             cnode = cnode.next
        #         cnode.next = newNode
        #     next_node =next_node.next

        # while head1 is not None:
        #     print(head1.val)
        #     head1 = head1.next

        # print("reverse list:")
        # while head is not None:
        #     print(head.val)
        #     head = head.next

        # while head and head1 is not None:
        #     if head.val != head1.val:
        #         return False
        #     head = head.next
        #     head1 = head1.next
        # return True
