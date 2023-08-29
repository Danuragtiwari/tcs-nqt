#[Check if a number is palindrome or not](https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/)



# Example 1:
# Input: N = 123
# Output: Not Palindrome Number
# Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

# n=123
n=122221
print(True) if str(n)==str(n)[::-1] else print(False)




