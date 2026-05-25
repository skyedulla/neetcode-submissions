# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_list = []
        subroot_list = []
        def compareTrees(root, subroot):
            #returns false if roots don't exist return False this is the end 
            if not root and not subroot:
                return True
            if (not subroot and root) or (not root and subroot):
                return False
            
            if subroot.val != root.val:
                return False

            if compareTrees(root.left, subroot.left) and compareTrees(root.right, subroot.right):
                return True

        queue = [root]
        while queue:
            for node in queue:
                if node.val == subRoot.val:
                    if compareTrees(node, subRoot):
                        return True
                    
                
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False
            
