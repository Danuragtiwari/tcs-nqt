# https://takeuforward.org/data-structure/find-gcd-of-two-numbers/


# Input: num1 = 4, num2 = 8
# Output: 4
n1=4
n2=8
def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)
    
print(gcd(n1,n2))