# 005. End Zeros

# Try to find out how many zeros a given number has at the end.

# Input: A positive Int
# Output: An Int.

# Example:

# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0


# Solve it like a number with division by 10 to the power of i

def end_zeros2(num: int) -> int:
        i = 1
        if num == 0 : return 1
        if num % 10 == 0 :
            for a in range(len(str(num))) :
                if num % 10**i == 0 :
                    i = i+1
                else :
                    return i-1
        else : 
            return 0

# Solve it like a string whith count zeros from the end of number

def end_zeros1(num: int) -> int:
    a = 0
    for i in range(len(str(num))) :
        if str(num)[-i-1] == '0' :
            a += 1
            if len(str(num)) == 1 :
                return 1
        else :
            return a

def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")