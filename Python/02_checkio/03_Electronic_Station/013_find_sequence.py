# Find Sequence

# “There’s nothing here...” sighed Nikola.
# “You’re kidding right? All treasure is buried treasure! It wouldn’t be
# treasure otherwise!” Said
# Sofia. “Here, take these.” She produced three shovels from a backpack that
# seemed to appear out of thin air.
# “Where did you get-”
# “Don’t ask questions. Just dig!” She hopped on the shovel and began digging
# furiously.
# CLUNK
# “Hey we hit something.” Stephen exclaimed in surprise.
# “It’s the treasure!” Sofia was jumping up and down in excitement.
# The trio dug around the treasure chest and pulled it out of the hole and
# wiped the dirt off. Sofia tried grabbing the lid but it was locked. Nikola
# studied the locking mechanism.
# “I’ve seen this type of lock before. It’s pretty simple. We just need to
# check whether there is a sequence of 4 or more matching numbers and output a
# bool.”
# “Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.

# You are given a matrix of NxN (4≤N≤10). You should check if there is a
# sequence of 4 or more matching digits. The sequence may be positioned
# horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

# find-sequence
# Input: A matrix as a list of lists with integers.
# Output: Whether or not a sequence exists as a boolean.

# Example:

# checkio([
#     [1, 2, 1, 1],
#     [1, 1, 4, 1],
#     [1, 3, 1, 6],
#     [1, 7, 2, 5]
# ]) == True
# checkio([
#     [7, 1, 4, 1],
#     [1, 2, 5, 2],
#     [3, 4, 1, 3],
#     [1, 1, 8, 1]
# ]) == False
# checkio([
#     [2, 1, 1, 6, 1],
#     [1, 3, 2, 1, 1],
#     [4, 1, 1, 3, 1],
#     [5, 5, 5, 5, 5],
#     [1, 1, 3, 1, 1]
# ]) == True
# checkio([
#     [7, 1, 1, 8, 1, 1],
#     [1, 1, 7, 3, 1, 5],
#     [2, 3, 1, 2, 5, 1],
#     [1, 1, 1, 5, 1, 4],
#     [4, 6, 5, 1, 3, 1],
#     [1, 1, 9, 1, 2, 1]
#     ]) == True

# How it is used:
# This concept is useful for games where you need to detect various lines of
# the same elements (match 3 games for example). This algorithm can be used for
# basic pattern recognition.

# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)


from typing import List
import numpy as np

# first solution (i don't like it)
def checkio(matrix: List[List[int]]) -> bool:
    # horiz
    for st in matrix:
        a = st[0]
        c = 0
        for j in range(len(st)):
            if st[j] == a:
                c += 1
            else:
                c = 0
                a = st[j]
            if c == 4:
                return True
    # vert
    for j in range(len(matrix)):
        a = matrix[0][j]
        c = 0
        for i in range(len(matrix)):
            cur = matrix[i][j]
            if cur == a:
                c += 1
            else:
                c = 0
                a = cur
            if c == 4:
                return True
    # diag
    # 1
    for i in range(len(matrix)):
        a = matrix[i][0]
        c = 0
        cur = a
        ii = i
        jj = 0
        while ii >= 0 and jj <= len(matrix):
            cur = matrix[ii][jj]
            if cur == a:
                c += 1
            else:
                c = 1
                a = cur
            ii -= 1
            jj += 1
            if c == 4:
                return True
    # 2
    for i in range(len(matrix)):
        a = matrix[i][0]
        c = 0
        cur = a
        ii = i
        jj = 0
        while 0 <= ii < len(matrix) and 0 <= jj < len(matrix):
            cur = matrix[ii][jj]
            if cur == a:
                c += 1
            else:
                c = 1
                a = cur
            ii += 1
            jj += 1
            if c == 4:
                return True
    # 3
    for j in range(len(matrix)):
        a = matrix[0][j]
        c = 0
        cur = a
        ii = 0
        jj = j
        while 0 <= ii < len(matrix) and 0 <= jj < len(matrix):
            cur = matrix[ii][jj]
            if cur == a:
                c += 1
            else:
                c = 1
                a = cur
            ii += 1
            jj += 1
            if c == 4:
                return True
    # 4
    for i in range(len(matrix)):
        a = matrix[i][len(matrix)-1]
        c = 0
        cur = a
        ii = i
        jj = len(matrix)-1
        while 0 <= ii < len(matrix) and 0 <= jj < len(matrix):
            cur = matrix[ii][jj]
            if cur == a:
                c += 1
            else:
                c = 1
                a = cur
            ii += 1
            jj -= 1
            if c == 4:
                return True
    return False



# second solution
def checkio(matrix: List[List[int]]) -> bool:
    
    def repeats_in_a_row(seq: List[int], num_of_rep: int) -> bool:
        cur = seq[0]
        c1 = 0
        for ii in range(len(seq)):
            if cur == seq[ii]:
                c1 += 1
            else:
                cur = seq[ii]
                c1 = 1
            if c1 == num_of_rep:
                return True
        return False  
    

    m1 = np.array(matrix)
    m2 = np.fliplr(m1)

    # rows and columns
    for i in range(len(matrix)):
        col = m1[:,i]
        row = m1[i,:]
        ans_col = repeats_in_a_row(col, 4)
        ans_row = repeats_in_a_row(row, 4)
        if ans_col or ans_row: 
            return True

    # diags
    for i in range(-len(matrix)+1, len(matrix)-1):
        d1 = m1.diagonal(i)
        d2 = m2.diagonal(i)
        ans_d1 = repeats_in_a_row(d1, 4)
        ans_d2 = repeats_in_a_row(d2, 4)
        if ans_d1 or ans_d2: 
            return True
    
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')