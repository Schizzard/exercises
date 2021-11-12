# Sum Numbers

# In a given text you need to sum the numbers while excluding any digits that form part of a word.

# The text consists of numbers, spaces and letters from the English alphabet.

# Input: A string.

# Output: An int.

# Example:

# sum_numbers('hi') == 0
# sum_numbers('who is 1st here') == 0
# sum_numbers('my numbers is 2') == 2
# sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
# sum_numbers('5 plus 6 is') == 11
# sum_numbers('') == 0

def sum_numbers(text: str) -> int:
    answ = 0
    words = text.split()
    for w in words :
        answ += int(w) if w.isnumeric() else 0
    return answ


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")