# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #I can explore the full left subtree before searching for the right one.

        """by exploring the tree using inorder traversal, I can figure out the node with 
        the smallest value based on first base case return. After it gets returned I will 
        return 0 count. Then I will process the first node, then I will process the right subtree.
        when count == k I will process the value of the node and add it to a variable and then.
        return that up the tree. I will set the variable to -1 this way the function will know that
        if that value is -1 it should keep searching. Then when the value gets changed to anything
        besides -1 it will stop exploring and return to the original call which will return the 
        value"""


        value = -1
        def countInorder(root):
            nonlocal k
            nonlocal value
            
            if k <= 0:
                return
            if root == None:
                return 

            countInorder(root.left)
            k -= 1
            if k == 0:
                value = root.val
            countInorder(root.right)

            
        countInorder(root)
        return value





