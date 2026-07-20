class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        pixel_condition = image[sr][sc]
        pixels_checked = set()
        def dfs(row, col):
            if min(row, col) < 0 or row >= len(image) or col >= len(image[0]):
                return
            if (row, col) in pixels_checked:
                return
            pixels_checked.add((row, col))
            if image[row][col] != pixel_condition:
                return

            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image