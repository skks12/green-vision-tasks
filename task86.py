import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor(neighbors, point):
    nearest = min(neighbors, key=lambda p: euclidean_distance(p, point))
    return nearest

neighbors = [(1, 2), (2, 3), (4, 5), (7, 8)]
point = (3, 3)
nearest = nearest_neighbor(neighbors, point)
print(f"The nearest neighbor to the point {point} is {nearest}")
