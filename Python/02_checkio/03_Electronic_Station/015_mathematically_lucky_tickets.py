# Mathematically Lucky Tickets

# Sofia cracks open the treasure chest. Inside are slips of paper with six 
# digit numbers on each slip.

# “What’s this?” She asks, quizzed. “Nikola, are these what I think they are?”
# “They look like lucky tickets! Look at how many there are, there must be 
# hundreds! Any of them could be a winner!”
# “Oh man! We could turn them into the lucky ticket commission and collect the 
# reward! I could pay my dad back for the spaceship!”
# “Er, you didn’t buy it yourself?” Stephen asked Sofia.
# “Well, not as such. I borrowed the money from my dad on the condition that 
# I’d pay him back. Now maybe I can!”
# Stephen sighed. “Well, let’s check the tickets to see if we have a winner.”
# “I have an idea. I brought my number cruncher 5000 along. I’ll just write a 
# quick function to find out if we won so we don’t have to do it all manually.” 
# Nikola interjected.
# “Quickly, quickly!” Sofia said. “I’m so excited!”

# The "Mathematically lucky tickets" concept is similar to the idea of the 
# Russian "Lucky tickets". It refers to the old public transport tickets that 
# had 6-digit numbers printed on them.

# You are given a ticket number and the combination of its digits can become a 
# mathematical expression by following these rules.

# 1. The digits of the number can be split into groups of numbers.
# 2. You cannot change the order of groups or digits.
# 3. Each group is treated as a one integer number. 1 and 2 would become 12
# 4. Operational signs (+, -, * and /) are placed between the groups.
# 5. Parenthesis are placed around subexpressions to eliminate any ambiguity
# in the evaluation order.

# For example:

#     * 238756 -> (2 * (38 + ((7 + 5) * 6)))
#     * 000859 -> (0 + (00 + (8 + (5 + 9))))
#     * 561403 -> (5 * (6 + (1 + (40 / 3))))

# The ticket is considered mathematically lucky if no combination of its digits 
# evaluates to 100. For example:

# * 000000 is obviously lucky, no matter which combination you construct it 
# always  evaluates to zero,
# * 707409 and 561709 are also lucky because they cannot evaluate to 100
# * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100
# * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100
# * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100

# The combination has to evaluate to 100 exactly to be counted as unlucky. 
# Fractions can occur in intermediate calculations (like in above examples for 
# 593347 and 271353) but the result must be an integer.

# Task: Given a 6-digit number of the ticket, the program should determine 
# whether it is mathematically lucky or not.

# Input: 6 digits as a string.
# Output: Is it mathematically lucky or not as a boolean.

# Example:
# checkio('000000') == True
# checkio('707409') == True
# checkio('595347') == False
# checkio('271353') == False

# How it is used: This is a nice game to improve mind-calculation skills. If 
# you have coder or math-geek friends, then you can give them this as a 
# challenge. Who’s code will check digits faster than the others? After solving 
# this task you will have the skills to cheat! ;-)

# Precondition: |digits| == 6



def goo(data: list):
    for comb in data:
        a = try_get_100(comb)
        return a

def try_get_100(comb: list):
    for i in range(len(comb)):
        res=[]
        if len(comb[:i]) > 0:
            res=res+comb[:i]
        if len(comb[i:i+2]) > 1:
            res.append(comb[i:i+2])
        else:
            res=res+comb[i:i+2]
        res=res+comb[i+2:]
        if len(res) > 2:
            try_get_100(res)
        else:
            return signs(res)
        

def signs(expr):
    return expr


def get_combinations(p='', data=''):
    c=[]
    d=[]
    for i in range(1, len(data)):
        left_1 = data[0:i]
        right_1 = data[i::]
        c=[*p, left_1, right_1]
        d.append(c)
        if len(right_1) > 1:
            e=get_combinations([*p,left_1], right_1)
            d.append(e)
    return d


# my solution
def checkio(data):
    c=get_combinations('', data)
    hmm = str(c).replace('[','').replace(']','').replace('\'','').replace(',','')
    seq = hmm.replace(' 1',', 1')
    sss = seq.split(', ')
    for i in range(len(sss)):
        sss[i] = sss[i].split() 
    return sss

# best solution
# def checkio(data):
#     return not any(abs(x - 100) < 0.00001 for x in comb_values(data))

# def comb_values(s):
#     yield int(s)
#     for i in range(len(s) - 1):
#         for l in comb_values(s[:i + 1]):
#             for r in comb_values(s[i + 1:]):
#                 yield l + r
#                 yield l - r
#                 yield l * r
#                 if r != 0: yield l * 1.0 / r



checkio('595347')
goo([[1, 2, 3, 4],[1, 2, 3, 4, 5]])
cc = checkio('123456')
try_get_100(cc)
print(cc)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
