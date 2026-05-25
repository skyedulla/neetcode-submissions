# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def detectNodeValues(value, root):
            value_detected = False
            queue = [root]
            while queue:
                for node in queue:
                    if node.val == value:
                        return True
                
                for i in range(len(queue)):
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)
                    queue.pop(0)
            return False
        
    
        if root.val == p.val or root.val == q.val:
            return root
        
        p_found = False
        q_found = False
        
        ancestors = []
        stack = [(root, [root])]

        while stack:
            node, current_path = stack.pop()

            if node.val == p.val:
                p_found = True
                ancestors = current_path
                break
            if node.val == q.val:
                q_found = True
                ancestors = current_path
                break

            if node.left:
                stack.append((node.left, current_path + [node.left]))
            if node.right:
                stack.append((node.right, current_path + [node.right]))
            
        #this finds both p and q and removes nodes from the stack that don't contain p and q
        while not p_found or not q_found:
            if q_found == True:
                both_found = detectNodeValues(p.val, ancestors[-1])
            else:
                both_found = detectNodeValues(q.val, ancestors[-1])
            
            if both_found:
                break
            else:
                ancestors.pop()

           
        LCA_node = root
        lowest_value = float('inf')
        for tree_node in ancestors:
            if tree_node.val < lowest_value:
                LCA_node = tree_node


        return LCA_node

        
                
        