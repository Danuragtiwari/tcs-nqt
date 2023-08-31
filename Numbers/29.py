# https://takeuforward.org/data-structure/find-the-sum-of-numbers-in-the-given-range/


# Example 1:
# Input: l=2, r=7
# Output: 27
# Explanation: 2+3+4+5+6+7=27. Therefore 27 is the answer.
l=2
r=7
sum1=0
for i in range(l,r+1):
    sum1+=i  
print(sum1)