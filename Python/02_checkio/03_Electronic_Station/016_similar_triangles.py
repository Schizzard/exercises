# Similar Triangles

# This is a mission to check the similarity of two triangles.
# You are given two lists as coordinates of vertices of each triangle.
# You have to return a bool. (The triangles are similar or not)

# Example:
# similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
# similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
# similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
		
# Input:
# Two lists as coordinates of vertices of each triangle.
# Coordinates is three tuples of two integers.
# Output: True or False.

# Precondition:
# -10 ≤ x(, y) coordinate ≤ 10

from math import sqrt
from typing import List, Tuple
Coords = List[Tuple[int, int]]

def cosA(ax,ay,bx,by): 
    return (ax*bx+ay*by) / (sqrt(ax**2+ay**2) * sqrt(bx**2+by**2))

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    triang_cos = []
    for a in [coords_1, coords_2]:
        vectors = []
        for i in range(len(a)):
            vectors.append(list(a[i][ii] - a[i-1][ii] for ii in range(len(a[i]))))
        cos_list = []
        for i in range(len(vectors)):
            cos_list.append(cosA(*vectors[i],*vectors[i-1]))
        cos_list.sort()
        triang_cos.append(cos_list)
    return triang_cos[0] == triang_cos[1]


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(1, 8), (1, 2), (2, 2)], [(3, 0), (4, 2), (5, 0)]))
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
