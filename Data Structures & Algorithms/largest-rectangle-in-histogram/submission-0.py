class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        span = [-1] * len(heights)
            

        stack = []
        for i in range(len(heights)):
            while stack != [] and heights[i] < heights[stack[-1]]:
                prev_index = stack.pop()
                span[prev_index] += i - prev_index
            stack.append(i)

        while stack:
            index = stack.pop()
            span[index] += len(heights) - index

        print(span)
        #This time I will do the span -1 since the first iterat
        for i in range(len(heights) -1, -1, -1):
            while stack != [] and heights[i] < heights[stack[-1]]:
                prev_index = stack.pop()
                span[prev_index] += prev_index - i
            stack.append(i)

        while stack:
            index = stack.pop()
            span[index] += index + 1

        print(span)

        max_area = 0
        for i in range(len(span)):
            area = heights[i] * span[i]
            max_area = max(max_area, area)

        return max_area


        
