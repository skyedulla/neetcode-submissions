# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l2.val == 0:
            return l1


        ptr1 = l1
        ptr2 = l2
        carry = 0
        curr_digit = 0

        total = l1.val + l2.val
        curr_digit = total % 10
        carry = total // 10
        total = 0
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        answer = ListNode(curr_digit)
        """we are changing the program because the loop requires ptr3 to be positioned
        in the space before the current node that should be added. and then it should add that node
        and then it should move to that node otherwise if there is no value to add simply stop the program"""
        
        
        ptr3 = answer
        still_calculating = True
        
        while still_calculating:
            if ptr1 != None:
                total += ptr1.val
                ptr1 = ptr1.next
            if ptr2 != None:
                total += ptr2.val
                ptr2 = ptr2.next
            if carry > 0:
                total += carry

            curr_digit = total % 10
            carry = total // 10
            total = 0

            if curr_digit > 0 or carry > 0:
                ptr3.next = ListNode(curr_digit)
                ptr3 = ptr3.next
            else:
                still_calculating = False

        return answer
        





        