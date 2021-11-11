# Max Digit

# You have a number and you need to determine which digit in this number 
# is the biggest.

# Input: A positive int.
# Output: An Int (0-9).

# Example:

# max_digit(0) == 0
# max_digit(52) == 5
# max_digit(634) == 6
# max_digit(1) == 1
# max_digit(10000) == 1

def max_digit(number: int) -> int:
    for i in range(9,-1,-1) :
        for x in str(number) :
            if int(x) == i : 
                return i



if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")