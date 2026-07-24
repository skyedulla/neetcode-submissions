from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
      
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        result = [0] * n

        result[start_node] = 1

        heap = [(start_node, 1)]

        while heap:
            curr, prob = heapq.heappop(heap)
            if result[curr] > prob:
                continue

            for next, chance in graph[curr]:
                if result[next] >= (prob * chance):
                    continue
                
                result[next] = prob * chance
                heapq.heappush(heap, (next, prob * chance))


        return result[end_node] 

        


