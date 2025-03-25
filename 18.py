# Travelling Salesman Problem (TSP)
import itertools
import sys
cities = [0, 1, 2]
distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
min_path = sys.maxsize
for perm in itertools.permutations(cities):
    path_cost = sum(distances[perm[i]][perm[i+1]] for i in range(len(perm)-1))
    min_path = min(min_path, path_cost)
print("Minimum TSP Cost:", min_path)
