# Replace Last

# In a given list the last element should become the first one. An empty list
# or list with only one element should stay the same

# Input: List.
# Output: Iterable.

# Example:
# replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
# replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
# replace_last([1]) == [1]
# replace_last([]) == []


# my solution
def replace_last(line: list) -> list:
    return line[-1:] + line[:-1]


# best solution
from collections import deque
def replace_last(items: list) -> deque:
    items = deque(items)
    items.rotate(1)
    return items

# best solution 2
def replace_last(items):
    if items:
        yield items[-1]
        for i in range(len(items)-1):
            yield items[i]


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
