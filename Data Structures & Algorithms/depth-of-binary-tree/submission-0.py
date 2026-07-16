# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def exploreDepth(root, curr_depth):
            if not root:
                return curr_depth
            
            return max(exploreDepth(root.left, curr_depth + 1), exploreDepth(root.right, curr_depth + 1))

        depth = exploreDepth(root, 0)
        return depth

        