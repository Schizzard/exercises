# All Upper I

# Check if a given string has all symbols in upper case. If the string is empty
# or doesn't have any letter in it - function should return True.

# Input: a string.
# Output: a boolean.

# Example:

# is_all_upper('ALL UPPER') == True
# is_all_upper('all lower') == False
# is_all_upper('mixed UPPER and lower') == False
# is_all_upper('') == True
# is_all_upper('444') == True
# is_all_upper('55 55 5') == True

# Precondition: a-z, A-Z, 1-9 and spaces

# My solution
def is_all_upper(text: str) -> bool:
    for ch in text :
        if ch.islower() == False : 
            next 
        else : return False 
    
    return True

# Best solution
def is_all_upper1(text: str) -> bool:
    return text.upper() == text

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")