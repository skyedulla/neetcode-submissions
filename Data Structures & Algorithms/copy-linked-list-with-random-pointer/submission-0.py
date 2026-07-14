"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #In our deep copy for a node to point to another node that node must be created and if a node is

        #Methods

        """
        1) Create an array of ListNode's in the exact same order as the deepcopy
        2) Then create two pointers in the original list and create two variables that constantly
        keep track of their index's
        3) Use the two pointers in the list to find the random pointer for each node by comparing 
        the nodes of the ptrs together. This will be O(n^2)
        4) When a match is found set the random pointer of the index of the 1st ptr to the node of
        the index of the second ptr. The array will be used to access to correct index
        """

        """
        The other approach would be to use two pointers to iterate through the array, and for 
        each iteration the second ptr iterates from the start to the end of the array until it finds
        a match for the node in the random pointer. It then finds the index and stores the index of
        the random node and the value of the list node.

        Then we take the array and we create a new Linked list using the values and index's for random
        pointers"""

        """The first method is better because we save space only using O(n) the minimum amount necessary.
        Both methods use the same time complexity which is also very efficient for an input size of 100.
        """


        array = []
        ptr = head
  
        while ptr != None:
            array.append(Node(ptr.val))
            ptr = ptr.next
        
        array.append(None)

        

        ptr1 = head
        indexptr1 = 0

        while ptr1 != None:
            array[indexptr1].next = array[indexptr1 + 1]
            
            ptr2 = head
            indexptr2 = 0
            while ptr1.random != ptr2:
                ptr2 = ptr2.next
                indexptr2 += 1

            array[indexptr1].random = array[indexptr2]

            ptr1 = ptr1.next
            indexptr1 += 1
        
        return array[0]





