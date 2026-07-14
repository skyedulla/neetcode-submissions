class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1

        ptr = self.head.next
        for i in range(index):
            ptr = ptr.next
        
        return ptr.val
        
    def addAtHead(self, val: int) -> None:
        next_node = self.head.next
        self.head.next = ListNode(val=val, next=next_node, prev=self.head)
        next_node.prev = self.head.next

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        prev_node = self.tail.prev
        self.tail.prev = ListNode(val, next=self.tail, prev=prev_node)
        prev_node.next = self.tail.prev

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        
        next_node = ptr.next
        ptr.next = ListNode(val=val, next=next_node, prev=ptr)
        next_node.prev = ptr.next
        
        self.size += 1

        
    def deleteAtIndex(self, index: int) -> None: 
        if index > self.size - 1:
            return 
        ptr = self.head
        for i in range(index):
            ptr = ptr.next

        node_before = ptr
        node_after = ptr.next.next
        node_before.next = node_after
        node_after.prev = node_before
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)