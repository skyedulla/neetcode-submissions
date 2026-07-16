# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        """we must right a recursive function that checks if the left and right subtrees
        of an inputted node's difference is less than 1
        
        if we pass the length of the longest branch of each root up to the parent node.
        Then we must check abs(left_branch_height - right_branch_height) <= 1.
        
        Then we must calculate the longest_branch of the current root.
        max(left_branch_height, right_branch_height) + 1"""


        def returnAndCompareHeight(root):
            if root == None:
                return 0, True

            left_branch_height, left_subtree_balanced = returnAndCompareHeight(root.left)
            right_branch_height, right_subtree_balanced = returnAndCompareHeight(root.right)
            if left_subtree_balanced != True or right_subtree_balanced != True:
                return 0, False
            
            if abs(left_branch_height - right_branch_height) <= 1:
                balanced = True
            else:
                balanced = False

            subtree_height = 1 + max(left_branch_height, right_branch_height)

            return subtree_height, balanced

        height, is_balanced = returnAndCompareHeight(root)
        return is_balanced







