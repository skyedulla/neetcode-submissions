# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for i in range(n + 1):
            if first:
                first = first.next
            else:
                return head.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head
