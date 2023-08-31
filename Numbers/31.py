# https://takeuforward.org/data-structure/program-to-add-two-fractions/




# Example 1:
# Input: 3/4 + 1/7 
# Output: 25/28
# Explanation: Since 3/4 + 1/7 = 25/28
from fractions import Fraction

fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 7)

result = fraction1 + fraction2

print(result)