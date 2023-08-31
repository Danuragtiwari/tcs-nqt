# https://takeuforward.org/data-structure/check-if-a-number-is-a-strong-number-or-not/


# Examples 1:
# Input: N = 145
# Output: Yes

def f(n):
    if n<=0:
        return 1
    return n*f(n-1)
# n=145
n=26
s=0
for i in str(n):
    s+=f(int(i))
if s==n:
    print("YES")
else:
    print("NO")