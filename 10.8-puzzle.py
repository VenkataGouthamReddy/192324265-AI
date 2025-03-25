from collections import deque

# Representation of the goal state
goal_state = "123456780"

# Input: initial state
initial_state = "123456708"

# Moves (up, down, left, right) represented as row and column changes
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Queue for BFS
queue = deque([(initial_state, [])])
visited = set()

while queue:
    current_state, path = queue.popleft()

    # Check if the state is valid
    if current_state == goal_state:
        print("Solution found:", path)
        break

    if current_state in visited:
        continue

    visited.add(current_state)

    # Get the position of the blank tile (represented as '0')
    blank_pos = current_state.index('0')
    row, col = divmod(blank_pos, 3)

    # Generate new states after each move
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(current_state)
            new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
            new_state = ''.join(new_state)

            if new_state not in visited:
                queue.append((new_state, path + [new_state]))

# If no solution is found
if current_state != goal_state:
    print("No solution found")
