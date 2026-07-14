import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        
        #Our simulation has proved that this algorithm will always result in left == right which will equal the row
        while low < high:
            mid = int(math.ceil((low + high) / 2))
            if target >= matrix[mid][0]:
                low = mid
            if target < matrix[mid][0]:
                high = mid - 1
        
        row = low

        left = 0
        right = len(matrix[row]) - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True         

        
        if left == right and matrix[row][left] == target:
            return True
        else:
            return False



        