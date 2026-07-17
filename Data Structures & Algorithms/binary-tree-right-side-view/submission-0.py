# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #if we perfor BFS on the tree we simply return the values of the last node in the queue each time
        if not root:
            return []

        queue = [root]
        next_queue = []

        answer = []

        while queue:
            first_node = True
            for node in queue:
                if first_node == True:
                    answer.append(node.val)
                    first_node = False
                if node.right:
                    next_queue.append(node.right)
                if node.left:
                    next_queue.append(node.left)

            queue = next_queue
            next_queue = []


        return answer