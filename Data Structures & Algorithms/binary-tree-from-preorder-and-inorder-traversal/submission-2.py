# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def splitlist(inorder):
            if not inorder:
                return

            curr = preorder.pop(0)
            root = TreeNode(curr)

            split_index = 0
            for i in range(len(inorder)):
                if inorder[i] == curr:
                    split_index = i 
            
            left_inorder = inorder[:split_index]
            right_inorder = inorder[split_index+1:]
            
            
            root.left = splitlist(left_inorder) 
            root.right = splitlist(right_inorder)

            
            return root



        return splitlist(inorder)

        

        

        
        