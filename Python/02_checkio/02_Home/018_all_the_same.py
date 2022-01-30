# All the Same

# In this mission you should check if all elements in the given list are equal.

# Input: List.
# Output: Bool.

# Example:

# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

# The idea for this mission was found on Python Tricks series by Dan Bader

# Precondition: all elements of the input list are hashable

from typing import List, Any

# fast solution (just start typing immediately)
def all_the_same1(elements: List[Any]) -> bool:
    if len(elements) == 0 :
        return True

    a=elements[0]
    for el in elements:
        if a != el :
            return False
        a = el
    return True 

# second solution (I had to think about it)
def all_the_same(elements: List[Any]) -> bool:
    return elements.count(elements[-1]) == len(elements) if len(elements) else True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
