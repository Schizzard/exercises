# Acceptable Password VI

# In this mission you need to create a password verification function.

# Those are the verification conditions:
# 1. the length should be bigger than 6;
# 2. should contain at least one digit, but it cannot consist of just digits;
# 3. having numbers or containing just numbers does not apply to the password 
# 4. longer than 9.
# 5. a string should not contain the word "password" in any case;
# 6. hould contain at least 3 different letters (or digits) even if it is 
#    longer than 10

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
# is_acceptable_password('aaaaaa1') == False
# is_acceptable_password('aaaaaabbbbb') == False

# How it’s used: For password verification form. Also it's good to learn how 
# the task can be evaluated.


# my solution
def is_acceptable_password(password: str) -> bool:
    return len({let for let in password}) > 2 and not("password" in password.lower()) and len(password) > 6 and (any([i.isdigit() for i in password]) and not(all([i.isdigit() for i in password])) or len(password) > 9)


# bes solution
def is_acceptable_password(password: str) -> bool:
    # c1 : length should be bigger than 6
    # c2 : contains at least one digit but it can't be all digits
    # c3 : having numbers is not required for password longer than 10
    # c4 : string should not contain word "password" in any case
    # c5 : consist of 3 different letters
    c1 = len(password) >= 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) >= 10
    c4 = 'password' not in password.lower()
    c5 = len(set(password)) >= 3
    return c1 and (c2 or c3) and c4 and c5


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
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
