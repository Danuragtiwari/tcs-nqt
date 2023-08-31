# https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive/

# Example 1:
# Input: X = 5
# Output: 120
# Explanation: 5! = 5*4*3*2*1
def f(n):
    if n<=0:
        return 1 
    return n*f(n-1)
n=5
print(f(n))
