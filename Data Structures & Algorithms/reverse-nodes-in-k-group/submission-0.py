# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """k is always less than or equal to the length of the list
        therefore we can reverse k nodes guaranteeing that we don't
        add Null or go past the end of the list."""

        rev = None
        curr = head

        for i in range(k):
            temp = rev
            rev = curr
            curr = curr.next
            rev.next = temp


        reached_end = False

        while reached_end != True:
            head2 = curr
            
            count = 0
            while curr != None and count < k:
                count += 1
                curr = curr.next

            
            if count >= k:
                rev2 = None
                curr2 = head2
                
                while curr2 != curr:
                    temp = rev2
                    rev2 = curr2
                    curr2 = curr2.next
                    rev2.next = temp
                
                head.next = rev2
                head = head2
            else:
                head.next = head2
                reached_end = True

        return rev 
        #our rev pointer will always be the start of the list because the first loop is 
        #guaranteed to run because k must be atleast equal to the number of nodes 
        #meaning it passes the condition nodes_left >= k








