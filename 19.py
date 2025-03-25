# A* Algorithm
from heapq import heappop, heappush
graph = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
h = {0: 3, 1: 2, 2: 0}
pq = [(h[0], 0)]
while pq:
    _, node = heappop(pq)
    for neighbor, cost in graph.get(node, []):
        heappush(pq, (cost + h[neighbor], neighbor))
print("A* Finished")
