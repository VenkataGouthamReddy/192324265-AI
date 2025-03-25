# Water Jug Problem (13, 13)
x, y = 0, 0
capacity_x, capacity_y = 4, 3  # Example capacities
goal = 2  # Example goal
while x != goal and y != goal:
    if x == 0:
        x = capacity_x
    elif y < capacity_y:
        transfer = min(x, capacity_y - y)
        x -= transfer
        y += transfer
    else:
        y = 0
    print(x, y)
