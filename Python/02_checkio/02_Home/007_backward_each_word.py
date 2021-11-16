# Backward Each Word

# In a given string you should reverse every word, but the words should stay in their places.

# Input: A string.
# Output: A string.

# Example:
# backward_string_by_word('') == ''
# backward_string_by_word('world') == 'dlrow'
# backward_string_by_word('hello world') == 'olleh dlrow'
# backward_string_by_word('hello   world') == 'olleh   dlrow'

# Precondition: The line consists only from alphabetical symbols and spaces.


def backward_string_by_word(text: str) -> str:
    word = ''
    sent = ''
    for i in range(text.__len__()) :
        if not text[i].isspace() :
            word = text[i] + word
        else :
            sent = sent + word + text[i]
            word = ''
    sent = sent + word
    return sent
            


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")