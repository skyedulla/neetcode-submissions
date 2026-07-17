# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValues(root, valid_numbers):
            if not root:
                return True

            if not (root.val >= valid_numbers[0] and root.val <= valid_numbers[1]):
                return False

        
            if checkValues(root.left, [valid_numbers[0], root.val - 1]) == False:
                return False
            if checkValues(root.right, [root.val + 1, valid_numbers[1]]) == False:
                return False

            return True


        #Edge Cases: root.left doesn't exist, root.right doesn't exist, they both don't exist

        if not root.left and not root.right:
            return True
        elif not root.left:
            return checkValues(root.right, [root.val + 1, float('inf')])
        elif not root.right:
            return checkValues(root.left, [-float('inf'), root.val - 1])

        #Main Case: both root.left and root.right exist
        else: 
            return checkValues(root.left, [-float('inf'), root.val - 1]) and checkValues(root.right, [root.val + 1, float('inf')])




