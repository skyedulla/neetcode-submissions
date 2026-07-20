"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        queue = deque([node])
        start_node = Node(node.val)

        cp_nodes = {node.val: start_node}
        

        while queue:
            graph_node = queue.popleft()
            curr_node = cp_nodes[graph_node.val]
            
            for neighbor in graph_node.neighbors:
                #add the deepcopy of the node if it hasn't been created and add the node to the queue
                if neighbor.val not in cp_nodes:
                    cp_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                
                #add the connection to the current deepcopyed nodes neighbors array
                curr_node.neighbors.append(cp_nodes[neighbor.val])

        return start_node
                


                
