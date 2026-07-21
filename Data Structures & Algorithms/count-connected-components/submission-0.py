from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        nodes_left = []
        for i in range(n):
            nodes_left.append(i)
        
        

        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])


        connected_components = 0
        while nodes_left:
            queue = deque()
            node = nodes_left.pop() 
            
            for connection in adjList[node]:
                if connection in nodes_left:
                    nodes_left.remove(connection)
                    queue.append(connection)
        

            while queue:
                node = queue.popleft()
                for connection in adjList[node]:
                    if connection in nodes_left:
                        nodes_left.remove(connection)
                        queue.append(connection)

            connected_components += 1

        return connected_components
