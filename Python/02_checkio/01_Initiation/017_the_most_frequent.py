# The Most Frequent

# You have a sequence of strings, and you’d like to determine the most 
# frequently occurring string in the sequence. It can be only one.

# Input: non empty list of strings.
# Output: a string.

# Example:

# most_frequent([
#     'a', 'b', 'c', 
#     'a', 'b',
#     'a'
# ]) == 'a'
# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    return sorted({w: data.count(w) for w in data}.items(), key=lambda x: -x[1])[0][0]


# best solution :D
from statistics import mode as most_frequent


# best solution
def most_frequent(data):
    return max(set(data), key=data.count)


if __name__ == "__main__":
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")

