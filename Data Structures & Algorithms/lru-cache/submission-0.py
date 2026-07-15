class LRUNode:

    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity
        self.size = 0

        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node_before = self.hash_map[key].prev
            node_after = self.hash_map[key].next
            node_before.next = node_after
            node_after.prev = node_before

            temp = self.head.next 
            self.head.next = self.hash_map[key]
            temp.prev = self.hash_map[key]
            
            self.hash_map[key].prev = self.head
            self.hash_map[key].next = temp

            return self.hash_map[key].val

        else:
            return -1
        

        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node_before = self.hash_map[key].prev
            node_after = self.hash_map[key].next
            node_before.next = node_after
            node_after.prev = node_before

            temp = self.head.next
            self.head.next = self.hash_map[key]
            temp.prev = self.hash_map[key]

            self.hash_map[key].next = temp
            self.hash_map[key].prev = self.head
            self.hash_map[key].val = value

        else:
            temp = self.head.next 
            self.head.next = LRUNode(key=key, val=value, prev=self.head, next=temp)
            temp.prev = self.head.next
            
            self.hash_map[key] = self.head.next

            self.size += 1

            if self.size > self.capacity:
                delete_node = self.tail.prev
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
                del self.hash_map[delete_node.key]

        
