# https://takeuforward.org/data-structure/check-if-the-given-number-is-harshador-nien-number/




# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.


n=378 
sum1=0
for i in str(n):
    sum1+=int(i)
if n%sum1==0:
    print(True)
else:
    print(False)