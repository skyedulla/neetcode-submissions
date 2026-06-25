import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heap.append(-stones[i])
        heapq.heapify(heap)
        
        while len(heap) > 2:
            if heap[1] <= heap[2]:
                index = 1
            else:
                index = 2
            

            if heap[0] == heap[index]:
                heapq.heappop(heap)
                heapq.heappop(heap)
            else:
                heap[0] = heap[0] - heap[index]
                if len(heap) == 3 and index == 2:
                    heap.pop()
                else:
                    heap[index] = heap.pop()
                    heapq._siftup(heap, index)
                    
                heapq._siftup(heap, 0)
                
        
        if len(heap) == 2:
            return abs(heap[0]) - abs(heap[1])
        else:
            return abs(heap[0])
        

            