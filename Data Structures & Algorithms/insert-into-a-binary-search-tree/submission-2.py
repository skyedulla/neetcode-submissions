# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)


        #the base cases are when the next node to traverse on is None, otherwise recursively call the function for child nodes
        def insertBST(node, val):
            if node == None:
                return TreeNode(val)

            if val < node.val:
                node.left = insertBST(node.left, val)

            elif val > node.val:
                node.right = insertBST(node.right, val)

            return node

        insertBST(root, val)

        return root
        