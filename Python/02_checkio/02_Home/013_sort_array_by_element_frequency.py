# Sort Array by Element Frequency

# Sort the given iterable so that its elements end up in the decreasing 
# frequency order, that is, the number of times they appear in elements. If 
# two elements have the same frequency, they should end up in the same order 
# as the first appearance in the iterable.

# Input: Iterable

# Output: Iterable

# Example:

# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == 
#                                       ['bob', 'bob', 'bob', 'carl', 'alex']

# Precondition: elements can be ints or strings

# The mission was taken from Python CCPS 109 Fall 2018. It's being taught for 
# Ryerson Chang School of Continuing Education by Ilkka Kokkarinen

def frequency_sort(items):
    my_dict = {}
    for elem in items :
        my_dict[elem] = items.count(elem)
    sorted_tuple = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    
    answ = []
    for i in sorted_tuple:
        for c in range(i[1]):
            answ.append(i[0])
    return answ

# Best solution
def frequency_sort1(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")