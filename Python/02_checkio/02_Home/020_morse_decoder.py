# Morse Decoder

# Your task is to decrypt the secret message using the Morse code .
# The message will consist of words with 3 spaces between them and 1 space 
# between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this 
# letter in uppercase.

# example

# Input: The secret message.

# Output: The decrypted text.

# Example:
# morse_decoder("... --- -- .   - . -..- -") == "Some text"
# morse_decoder("..--- ----- .---- ---..") == "2018"
# morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") \
#                                                        == "It was a good day"

# How it is used: For cryptography and spy work.

# Precondition :
# 0 < len(message) < 100
# The message will consists of numbers and English letters only.

from ntpath import join


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "+": " "
}

# first solution (~20 min)
def morse_decoder(code):
    words = code.split("   ")
    answer_word = ""
    answer = []
    for word in words :
        letters = word.split(" ")
        for letter in letters:
            answer_word = answer_word + MORSE[letter]
        answer.append(answer_word)
        answer_word = ""
    return str(" ".join(answer)).capitalize()   

# second solution (~60 min)
def morse_decoder(code):
    ww=[]
    for w in code.split("   "):
        ww.append("".join(MORSE[l] for l in w.split(" ")))
    return " ".join(ww).capitalize()


# best solution
morse_decoder = lambda code: "".join([MORSE[i] for i in code.replace("   ", " + ").split()]).capitalize()


# best solution
def morse_decoder(c,k="y7ac-it-oe4gw5qr1zx-jb-p-6kf0du9-s--m--n2lv-3h---8"):
 return ' '.join(''.join(k[int('1'+i.replace('.','3').replace('-','0'),6)%52]
  for i in j.split()) for j in c.split('   ')).capitalize()


if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- ..."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert (
        morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
        == "It was a good day"
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
