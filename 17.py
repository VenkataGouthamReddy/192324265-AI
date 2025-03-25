# DFS Implementation
graph = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
stack = [0]
visited = set()
while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        stack.extend(graph.get(node, []))
print("DFS Order:", visited)
