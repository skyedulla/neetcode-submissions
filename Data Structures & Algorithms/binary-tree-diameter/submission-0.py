# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """the diameter between any two nodes is the depth of each node excluding the root
        summed together."""


        #we can find the diameter of each node in the tree assuming it is a root
        #then we can 

        #the diameter of any node in the tree is equal to the longest_branch of the 
        # longest_branch_of_left_child + longest_branch_of_right_child.

        

        def longestBranch(root):
            if not root.left and not root.right:
                return 0, 0

            diameter = 0

            if root.left:
                left_branch, left_diameter = longestBranch(root.left)
                diameter += 1
            else:
                left_branch = 0
                left_diameter = 0
            
            if root.right:
                right_branch, right_diameter = longestBranch(root.right)
                diameter += 1
            else:
                right_branch = 0
                right_diameter = 0

            longest_branch = max(left_branch, right_branch) + 1


            diameter += left_branch + right_branch
            max_diameter = max(diameter, left_diameter, right_diameter)

            return longest_branch, max_diameter


        longest_branch, max_diameter = longestBranch(root)
    
        return max_diameter



        
        
        