# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        
        #create a new linked list with a starting node 0
        ans = ListNode(0)
        #create a pointer to the start of the new linked list
        curr = ans

        #while first and second both exist
        while first and second:
            #if the value of the first element of list1 is less than that of the second
            #set curr.next to equal that node. then move the first pointer to the next node in list 1
            if first.val < second.val:
                curr.next = first
                first = first.next
                curr = curr.next
            #if the value of the second list element is lower than 
            else:
                curr.next = ListNode(second.val)
                second = second.next
                curr = curr.next

        if first:
            curr.next = first
        else:
            curr.next = second

        return ans.next