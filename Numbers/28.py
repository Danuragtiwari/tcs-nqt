# Sum of digits of a number https://takeuforward.org/data-structure/sum-of-digits-of-a-number/


# Example 1:
# Input: N = 472
# Output: 13
# Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

n=472 
sum1=0
for i in str(n):
    sum1+=int(i)
print(sum1)