import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if self.min_heap == []:
            self.min_heap.append(num)
        elif self.max_heap == []:
            if num > self.min_heap[0]:
                self.min_heap.append(num)
            else:
                self.max_heap.append(-num)
        else:
            if -self.max_heap[0] > num:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            
        difference = len(self.max_heap) - len(self.min_heap)

        if abs(difference) > 1:
            if difference > 0:
                new_min = heapq.heappop(self.max_heap)
                new_min *= -1
                heapq.heappush(self.min_heap, new_min)
            else:
                new_max = heapq.heappop(self.min_heap)
                new_max *= -1
                heapq.heappush(self.max_heap, new_max)



    def findMedian(self) -> float:
        if not self.min_heap:
            return self.max_heap[0]
        if not self.max_heap:
            return self.min_heap[0]

        difference = len(self.max_heap) - len(self.min_heap)
        if difference == 0:
            return (self.min_heap[0] + (-(self.max_heap[0]))) / 2
        elif difference == -1:
            return self.min_heap[0]
        elif difference == 1:
            return -self.max_heap[0]
        
        