# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def mergeLists(list1,list2):
            if not list1 and not list2:
                return list1
            if not list1:
                return list2
            if not list2:
                return list1
            
            p1 = list1
            p2 = list2
            if p1.val < p2.val:
                head = p1
                headptr = head
                p1 = p1.next
            else:
                head = p2
                headptr = head
                p2 = p2.next

            while p1 and p2:
                if p1.val <= p2.val:
                    headptr.next = p1
                    p1 = p1.next
                    headptr = headptr.next
                else:
                    headptr.next = p2
                    p2 = p2.next
                    headptr = headptr.next
            
            if p1:
                headptr.next = p1
            elif p2:
                headptr.next = p2

            return head

        merged_lists = []

        while len(lists) > 1:
            for i in range(1, len(lists), 2):
                list1 = lists[i - 1]
                list2 = lists[i]
                new_list = mergeLists(list1,list2)
                merged_lists.append(new_list)
            
            if len(lists) % 2 == 1:
                merged_lists.append(lists[-1])
            lists = merged_lists
            merged_lists = []
        
        return lists[0]
           