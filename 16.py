# BFS Implementation
from collections import deque
graph = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
queue = deque([0])
visited = set()
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        queue.extend(graph.get(node, []))
print("BFS Order:", visited)
