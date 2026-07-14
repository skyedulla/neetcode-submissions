# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return

        """Splitting the list in half"""
        fast = head.next
        slow = head

        while fast and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        
        list2 = slow.next
        slow.next = None
        
        
        """List Reversal"""
        rev = None
        curr = list2 #this is correct for sure 

        while curr != None:
            temp = rev
            rev = curr
            curr = curr.next
            rev.next = temp
            

        
        """Building Intertwined List"""
        ptr1 = head
        ptr2 = rev

        while ptr2 != None:
            rol = ptr1.next #store the rest of the list in a variable rol
            ptr1.next = ptr2 #set ptr1 equal to the next element in the reversed list
            ptr2 = ptr2.next # move the reversed list forward

            ptr1 = ptr1.next #iterate the pointer to move to the newly added element
            ptr1.next = rol 

            ptr1 = ptr1.next

        
        
        

        
        
        






        