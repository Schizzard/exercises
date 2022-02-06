# Surjection Strings

# Maybe it's a cipher? Maybe, but we don’t know for sure.
# Maybe you can call it "homomorphism" ? I wish I knew this word before.
# You need to check that the String A is isometric to the String B. This means 
# that a character from String A can become a match for characters from 
# String B.

# One character from String A can correspond only to one character from 
# String B. Two or more characters of String B can correspond to one character 
# of String A.


# Input: Two arguments. String A and String B.
# Output: Boolean.

# Example:
# isometric_strings('add', 'egg') == True
# isometric_strings('foo', 'bar') == False
# isometric_strings('', '') == True
# isometric_strings('all', 'all') == True
# isometric_strings('gogopy', 'doodle') == False

# Precondition:
# both strings are the same length

def isometric_strings(a, b):
    d = {}
    for i in range(len(a)):
        if a[i] != b[i]:
            if not (a[i] in d.keys()) or d[a[i]] == b[i]:
                d[a[i]] = b[i]
            else:
                return False
    return True


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
