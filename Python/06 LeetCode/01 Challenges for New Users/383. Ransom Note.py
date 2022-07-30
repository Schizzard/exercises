# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rl = list(ransomNote)
        ml= list(magazine)
        for i in range(len(rl)):
            if rl[i] in ml:
                ml.pop(ml.index(rl[i]))
            else:
                return False
        return True



ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

a = Solution
assert a.canConstruct2(a, ransomNote=ransomNote, magazine=magazine) == True
