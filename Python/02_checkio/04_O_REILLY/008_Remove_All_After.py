# Remove All After

# Not all of the elements are important. What you need to do here is to remove
# all of the elements after the given one from list.

# example

# For illustration, we have an list [1, 2, 3, 4, 5] and we need to remove all
# the elements that go after 3 - which is 4 and 5.

# We have two edge cases here: (1) if a cutting element cannot be found, then
# the list shouldn't be changed; (2) if the list is empty, then it should
# remain empty.

# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).

# Example:
# remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
# remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]


from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    return items if border not in items else items[0:items.index(border)+1]


# best solution
def remove_all_after(items: List, border: int) -> Iterable:
    for item in items:
        yield item
        if item == border:
            return


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")