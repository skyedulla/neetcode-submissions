class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(row, col, flow, prev_value):
            if min(row, col) < 0 or row >= len(heights) or col >= len(heights[0]):
                return
            if heights[row][col] < prev_value:
                return 

            if (row, col) not in flow_data:
                flow_data[(row, col)] = set()

            if flow in flow_data[(row, col)]:
                return
            
            
            flow_data[(row, col)].add(flow)

            dfs(row + 1, col, flow, heights[row][col])
            dfs(row - 1, col, flow, heights[row][col])
            dfs(row, col + 1, flow, heights[row][col])
            dfs(row, col - 1, flow, heights[row][col])


        flow_data = {}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
        
                if i == 0 or j == 0:
                    dfs(i, j, 'P', heights[i][j])
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, 'A', heights[i][j])
                

        res = []
        for coors, access in flow_data.items():
            row, col = coors
            if len(access) == 2:
                
                res.append([row, col])

        return res



