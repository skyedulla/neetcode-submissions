# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we must do a DFS search through the array passing down a parameter through 
        #each call stack the compares the previous parents max to the current node 
        #and updates the max. 

        #the call stack is sent all the way down 

        #for each call in the call stack, the call will compare its own value to
        #the max_value passed down to it from the parent. If the nodes value is greater 
        #than or equal to the passed down parameter then we return 1 + whatever was returned
        #by both children


        def describeNodes(root, ances_max):
            if not root:
                return 0
            
            good_nodes = 0
            good_nodes += describeNodes(root.left, max(root.val, ances_max))
            good_nodes += describeNodes(root.right, max(root.val, ances_max))

            if root.val >= ances_max:
                return good_nodes + 1
            else:
                return good_nodes

        return describeNodes(root, root.val)







