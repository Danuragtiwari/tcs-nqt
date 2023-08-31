# https://takeuforward.org/combinatorics/factors-of-a-given-number/


# Example 1:
# Input: n = 6
# Output: 1,2,3,6
# Explanation: 6 is divisible by 1,2,3,6

n=6 
for i in range(1,n+1):
    if n%i==0:
        print(i)