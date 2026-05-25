# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), TypeVarTuple:
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, current_sum):
            if not root:
                return False

            current_sum += root.val

            if current_sum == targetSum and not root.left and not root.right:
                return True
            
            left_branch_hit = dfs(root.left, current_sum)
            if left_branch_hit:
                return True
            
            right_branch_hit = dfs(root.right, current_sum)
            if right_branch_hit:
                return True

            return False

        current_sum = 0
        return dfs(root, current_sum)
        
            
                #after a stack.pop() we are visiting a node that was already 
                #traversed on the left side so we should check the right side and then go left agin
            
        