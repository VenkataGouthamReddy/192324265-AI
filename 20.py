# Map Coloring for CSP
colors = ['Red', 'Green', 'Blue']
regions = ['A', 'B', 'C']
assignment = {}
for region in regions:
    for color in colors:
        if color not in assignment.values():
            assignment[region] = color
            break
print("Color Assignment:", assignment)
