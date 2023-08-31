#Check if a number is perfect number #https://takeuforward.org/data-structure/check-whether-a-number-is-perfect-number-or-not/


# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.
n=28
sum1=0
for i in range(1,n-1):
    if n%i==0:
        sum1+=i 
if sum1==n:
    print(True)
else:
    print(False)