#[Program to find sum of GP Series](https://takeuforward.org/data-structure/program-to-find-sum-of-gp-series/)


# Example 1:
# Input: a=1 , r=0.5 , n=3
# Output: 1.75
# Explanation: The sum of given GP Series is 1.75


a=1
r=0.5
n=3 
if r>1:
    print(a*(r**(n)-1)/(r-1))
else:
    print(a*(1-(r)**(n))/(1-r))

