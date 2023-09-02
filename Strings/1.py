# [palindrom]  https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/


# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

s='ABCDCBA'
if s==s[::-1]:
    print("TRUE")
else:
    print(False)