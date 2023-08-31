# https://takeuforward.org/data-structure/print-all-prime-factors-of-the-given-number/



# Example 1:
# Input: N = 12
# Output: 2,2,3
# Explanation: These are the prime factors of 12.

n=12
i = 2
while n > 1:
    if n % i == 0:
        while n % i == 0:
            print(i, end=' ')
            n = n // i
    i += 1