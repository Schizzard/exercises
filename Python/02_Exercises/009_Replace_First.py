# Replace First

# In a given list the first element should become the last one. An empty list 
# or list with only one element should stay the same.

# Input: List.
# Output: Iterable.

# Example:

# replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# replace_first([1]) == [1]

from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items.__len__() == 0 or items.__len__() == 1 : 
        return items
    items_1 = items[1:] + [items[0]]
    return items_1

## Best solutions
# Change items IN-PLACE.
def replace_first1(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first2(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first3(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")