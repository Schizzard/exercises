# Acceptable Password V

# In this mission you need to create a password verification function.

# Those are the verification conditions:

# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# having numbers or containing just numbers does not apply to the password 
# longer than 9.
# a string should not contain the word "password" in any case.

# Input: A string.
# Output: A bool.

# Example:

# is_acceptable_password('short') == False
# is_acceptable_password('short54') == True
# is_acceptable_password('muchlonger') == True
# is_acceptable_password('ashort') == False
# is_acceptable_password('muchlonger5') == True
# is_acceptable_password('sh5') == False
# is_acceptable_password('1234567') == False
# is_acceptable_password('12345678910') == True
# is_acceptable_password('password12345') == False
# is_acceptable_password('PASSWORD12345') == False
# is_acceptable_password('pass1234word') == True

# How it’s used: For password verification form. Also it's good to learn how 
# the task can be evaluated.

def is_acceptable_password(password: str) -> bool:
    return not("password" in password.lower()) and len(password) > 6 and (any([i.isdigit() for i in password]) and not(all([i.isdigit() for i in password])) or len(password) > 9)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
