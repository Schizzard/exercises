# Words Order

# You have a text and a list of words. You need to check if the words in a list 
# appear in the same order as in the given text.

# Cases you should expect while solving this challenge:

# a word from the list is not in the text - your function should return False;
# any word can appear more than once in a text - use only the first one;
# two words in the given list are the same - your function should return False;
# the condition is case sensitive, which means 'hi' and 'Hi' are two different 
# words; the text includes only English letters and spaces.

# Input: Two arguments. The first one is a given text, the second is a list of 
# words.
# Output: A bool.

# Example:

# words_order('hi world im here', ['world', 'here']) == True
# words_order('hi world im here', ['here', 'world']) == False
# words_order('hi world im here', ['world']) == True
# words_order('hi world im here',
#  ['world', 'here', 'hi']) == False
# words_order('hi world im here',
#  ['world', 'im', 'here']) == True
# words_order('hi world im here',
#  ['world', 'hi', 'here']) == False
# words_order('hi world im here', ['world', 'world']) == False
# words_order('hi world im here',
#  ['country', 'world']) == False
# words_order('hi world im here', ['wo', 'rld']) == False
# words_order('', ['world', 'here']) == False


# first solution (~50 min)
def words_order(text: str, words: list) -> bool:
    if len(words) != len(dict.fromkeys(words , 1)): return False
    for w in text.split():
        if w == words[0]: words.remove(w)
        if len(words) == 0: return True
    return False

# best solution
def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

# best solution
def words_order(text: str, words: list) -> bool:
    # A word that appears twice make this simple.
    if len(set(words)) != len(words):
        return False
    # Look for words indexes with a simple iteration on text words.
    words = {word: -1 for word in words}  # A dict remembers insertion order.
    for n, text_word in enumerate(text.split()):
        if text_word in words and words[text_word] == -1:
            words[text_word] = n
    # Make sure all words are in the text and indexes are increasing.
    last = -1
    for index in words.values():
        if index <= last:
            return False
        last = index
    return True


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
