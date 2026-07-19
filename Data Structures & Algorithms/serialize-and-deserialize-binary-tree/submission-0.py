# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        array = []
        array.append(root.val)
        array.append(',')

        queue = [root]
        next_queue = []

        while queue:
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                    array.append(node.left.val)
                    array.append(',')
                else:
                    array.append('#')
                    array.append(',')

                if node.right:
                    next_queue.append(node.right)
                    array.append(node.right.val)
                    array.append(',')
                else:
                    array.append('#')
                    array.append(',')


            queue = next_queue
            next_queue = []

        return "".join(str(item) for item in array)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        start_index = 0
        first_number = ''
        while data[start_index] != ',':
            first_number += data[start_index]
            start_index += 1
        start_index += 1
        first_number = int(first_number)

        root = TreeNode(first_number)
        queue = [root]
        next_queue = []
        inputs_required = 2
        
        inputs = []
        number = ""
        for i in range(start_index, len(data)):
            if data[i] == ',':
                if number:
                    inputs.append(int(number))
                    number = ""
            elif data[i] == '#':
                inputs.append(None)
            else:
                number += data[i]

            if len(inputs) == inputs_required:

                i_ptr = 0
                for node in queue:
                    if inputs[i_ptr] != None:
                        node.left = TreeNode(inputs[i_ptr])
                        next_queue.append(node.left)
                    else:
                        node.left = None
                    i_ptr += 1
                    if inputs[i_ptr] != None:
                        node.right = TreeNode(inputs[i_ptr])
                        next_queue.append(node.right)
                    else:
                        node.right = None
                    i_ptr += 1

                queue = next_queue
                next_queue = []
                inputs_required = len(queue) * 2
                inputs = []
        
        return root

               

            




            

        
       