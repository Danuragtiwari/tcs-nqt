# https://takeuforward.org/data-structure/find-lcm-of-two-numbers/






# Example 1:
# Input: num1 = 4,num2 = 8
# Output: 8
n1=4
n2=8
n3=n1*n2


def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)
    
print(n3//gcd(n1,n2))