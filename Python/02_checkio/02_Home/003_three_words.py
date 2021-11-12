# Three Words

# Let's teach the Robots to distinguish words and numbers.

# You are given a string with words and numbers separated by whitespaces (one 
# space). The words contains only letters. You should check if the string 
# contains three words in succession . For example, the string "start 5 one 
# two three 7 end" contains three words in succession.

# Input: A string with words.
# Output: The answer as a boolean.

# Example:

# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False

# How it is used: This teaches you how to work with strings and introduces 
# some useful functions.

# Precondition: The input contains words and/or numbers. There are no mixed 
# words (letters and digits combined).
# 0 < len(words) < 100

# hard (first answ)
def checkio(words: str) -> bool:
    return any(all(list(map(str.isalpha, words.split()[i:i+3]))) for i in range(len(words.split())-2))

# easy (second answ, just for "nice.")
def checkio1(words: str) -> bool:
    my_list = words.split()                             # get list of words
    count_of_3_words = len(my_list)-2                   # get countof possible tripples
    for i in range(count_of_3_words) :                  # try all tripples
        tripple = my_list[i:i+3]                        # get tripple
        true_table = list(map(str.isalpha, tripple))    # check all item is word - get list true/false
        if all(true_table) : return True                # if all is true - return true
    return False                                        # if there are no true - return false

# Best solutions
checkio3=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())

def checkio2(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World 1"))
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")