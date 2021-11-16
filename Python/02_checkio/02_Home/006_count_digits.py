# Count Digits

# You need to count the number of digits in a given string.

# Input: A Str.
# Output: An Int.

# Example:
# count_digits('hi') == 0
# count_digits('who is 1st here') == 1
# count_digits('my numbers is 2') == 1
# count_digits('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 8
# count_digits('5 plus 6 is') == 2
# count_digits('') == 0

def count_digits(text: str) -> int:
    i = 0
    for c in text :
        if c.isnumeric() :
            i += 1
    return i

# Best solution
def count_digits1(text: str) -> int:
    return sum(c.isdigit() for c in text)

def count_digits2(text: str) -> int:
    return sum(map(str.isdigit, text))

if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")