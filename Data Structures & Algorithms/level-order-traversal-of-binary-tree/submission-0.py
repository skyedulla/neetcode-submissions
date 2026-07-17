# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = [root]
        next_queue = []
        answer = []
        
        while queue != []:
            level = []
            for node in queue:
                level.append(node.val)
            answer.append(level)

            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue
            next_queue = []

        return answer


            