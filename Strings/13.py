# https://takeuforward.org/data-structure/check-if-two-strings-are-anagrams-of-each-other/


# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

s1='CAT'
s2='ACT'
if len(s1)==len(s2) and (all(i in s2 for i in s1)):
    print(True)
else:
    print(False)