# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        """
        Based on our initial investigation of the problem. The simplest and most efficient
        way to solve the problem is to use postorder traversal and process each branch 
        carefully by doing the following.

        For each node we will compute the maximum path sum including that node. Then we will
        pass the maximum path sum including that node up to the parent node and let the 
        function decide how to use the path sum of its subtree

        """

        """The value that we are passing up to the parent call stack needs to be a branch
        of the current subtree. It can't include left and right.
        """

        def sumSubTrees(root):
            if not root:
                return 0

            left_subtree_max_path_sum = sumSubTrees(root.left)
            right_subtree_max_path_sum = sumSubTrees(root.right)
            
            current_root_max_path_sum = max(
            root.val, 
            root.val + right_subtree_max_path_sum, 
            root.val + left_subtree_max_path_sum, 
            root.val + left_subtree_max_path_sum + right_subtree_max_path_sum)


            if current_root_max_path_sum > max_val[0]:
                max_val[0] = current_root_max_path_sum
            
            return max(root.val, root.val + left_subtree_max_path_sum, root.val + right_subtree_max_path_sum)

        max_val = [root.val]
        sumSubTrees(root)
        return max_val[0]



