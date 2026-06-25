import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            distance = ((xi - 0) ** 2 + (yi - 0) ** 2) ** 0.5
            heap.append((distance, [xi, yi]))

        heapq.heapify(heap) #create the heap based on the [0] index of each tuple

        closest_coors = []
        for i in range(k):
            distance, coors = heapq.heappop(heap)
            closest_coors.append(coors)
        
        return closest_coors
        