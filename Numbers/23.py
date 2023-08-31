# https://takeuforward.org/data-structure/check-if-a-number-is-automorphic-number/




# Input Format: N = 76
# Result: Automorphic Number
# Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.

# n=76
n=25
if int(str(n**2)[-2:])==n:
    print('yes')
else:
    print('no')