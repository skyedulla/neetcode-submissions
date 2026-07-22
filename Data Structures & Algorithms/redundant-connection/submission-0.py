from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        #when the duplicate is detected I can unwind the callstack
        #from the end and append nodes to a list until the duplicate
        #node is reached again
        

        #the return value of the function represents whether
        #to continue recursing (False) or whether to stop (True)
        def dfs(node, prev_node, path):
            if node in path:
                graph_cycle.append(node)
                return True

            if adjList == []:
                return False

            path.add(node)
            for connection in adjList[node]:
                if connection == prev_node:
                    continue
        
                duplicate_found = dfs(connection, node, path)
                if duplicate_found:
                    if graph_cycle[-1] == graph_cycle[0] and len(graph_cycle) > 1:
                        return True
                        
                    graph_cycle.append(node)
                    return True
                
            path.remove(node)   

       
        graph_cycle = []
        dfs(edges[0][0], None, set())
        # I could query the nodes in graph cycle with the dictionary, but that would require adjustments
        # the other route is to iterate through edges backwards until I find a match in the list.
        
        # that would be the quickest way or I could check the index of each edge in the cycle
        #and prune the search when it goes past the min index from the back of edges.

        print(graph_cycle)
        for i in range(len(edges) - 1, -1, -1):
            for j in range(len(graph_cycle) - 1):
                if ([graph_cycle[j], graph_cycle[j + 1]] == edges[i] 
                or [graph_cycle[j + 1], graph_cycle[j]] == edges[i]):
                    return edges[i]

        



                