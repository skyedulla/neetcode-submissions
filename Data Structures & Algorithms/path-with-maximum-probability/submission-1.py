from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
      
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        result = [0] * n

        result[start_node] = -1

        maxheap = [(-1, start_node)]

        while maxheap:
            prob, curr = heapq.heappop(maxheap)
            if result[curr] < prob:
                continue

            for next, chance in graph[curr]:
                new_prob = abs(prob * chance) * -1


                if result[next] <= (new_prob):
                    continue
                
                result[next] = new_prob
                heapq.heappush(maxheap, (new_prob, next))


        return abs(result[end_node])

        


