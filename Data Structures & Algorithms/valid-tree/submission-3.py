class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges:
            return True

        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        if len(adjList) < n:
            return False
        

        def dfs(node, parent_node):
            if node in node_pool:
                return False

            node_pool.add(node)

            if adjList[node] == []:
                return True

            
            for connection in adjList[node]:
                if connection == parent_node:
                    continue
                if not dfs(connection, node):
                    return False

            return True
                


        node_pool = set()
        root = edges[0][0]
        res = dfs(root, None)
        print(len(node_pool))

        if len(node_pool) == n:
            return res
        else:
            return False





