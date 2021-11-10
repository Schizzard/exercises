# Split Pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

# Input: A string.
# Output: An iterable of strings.

# Example:

# split_pairs('abcd') == ['ab', 'cd']
# split_pairs('abc') == ['ab', 'c_']

# Precondition: 0<=len(str)<=100

def split_pairs(a):
    my_list = list()
    pair = ''
    if str(a).__len__() == 0 : return my_list 

    for let in str(a) :
        pair += let
        if str(pair).__len__() == 2 :
            my_list.append(pair)
            pair = ''
    if pair != '' : 
        pair += '_'
        my_list.append(pair)
        pair = ''
    return my_list

# Best solution
def split_pairs2(a):
    a += '_' if len(a) % 2 else ''
    return [a[i:i + 2] for i in range(0, len(a), 2)]


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
