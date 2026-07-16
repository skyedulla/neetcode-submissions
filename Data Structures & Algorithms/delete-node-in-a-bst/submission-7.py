# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def findMax(root):
            if root.right:
                root = root.right
                while root.left or root.right:
                    if root.right:
                        root = root.right
                    else:
                        root = root.left
            
            return root


        def delete(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:
                if root.left and root.right:
                    max_node = findMax(root.left)

                    right_branch = root.right
                    left_branch = delete(root.left, max_node.val)
                    
                    max_node.left = left_branch
                    max_node.right = right_branch
                    return max_node

                elif root.left:
                    return root.left

                elif root.right:
                    return root.right
                else:
                    return None

            return root

        root = delete(root, key)
        return root

        """When we reach the node that we need to delete our goal is to construct
        a new tree and return a pointer. 
        
        If the branch has two children, then we execute an operation that changes the left
        branch and saves the right branch and returns a reconstructed tree.
        
        If the branch has a single right child we store the right branch in a replace
        variable, we execute delete on the right branch and set it equal to a new_variable
        right_branch which will return an updated branch using the same delete logic.
        
        So we are replacing the right branch of the original with an updated tree
        that deleted root.right and then we are adding that branch to root.right and replacing
        the original node with that branch.
        
        For the cases where we are replacing a single child we also set the opposite pointer to None
        to delete the old branch that it used to point to. 
        
        In the case where the node that we are deleting has no left and right branches,
        we simply return None because that will delete the node."""
                
                    


        