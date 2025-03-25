# Missionaries and Cannibals Problem
from collections import deque
queue = deque([((3, 3, 1), [])])
visited = set()
goal = (0, 0, 0)
while queue:
    state, path = queue.popleft()
    if state == goal:
        print(path)
        break
    if state in visited:
        continue
    visited.add(state)
    queue.extend([(new_state, path + [new_state]) for new_state in [(2, 3, 0), (3, 2, 0)] if new_state not in visited])
