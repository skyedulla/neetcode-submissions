class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(row, col, stream, prev_value):
            if min(row, col) < 0 or row >= len(heights) or col >= len(heights[0]):
                return
            if heights[row][col] < prev_value:
                return 

            if (row, col) not in stream_data:
                stream_data[(row, col)] = set()

            if stream in stream_data[(row, col)]:
                return
            
            
            stream_data[(row, col)].add(stream)

            dfs(row + 1, col, stream, heights[row][col])
            dfs(row - 1, col, stream, heights[row][col])
            dfs(row, col + 1, stream, heights[row][col])
            dfs(row, col - 1, stream, heights[row][col])


        stream_data = {}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
        
                if i == 0 or j == 0:
                    dfs(i, j, 'P', heights[i][j])
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, 'A', heights[i][j])
                

        res = []
        for coors, access in stream_data.items():
            row, col = coors
            if len(access) == 2:
                res.append([row, col])

        return res



