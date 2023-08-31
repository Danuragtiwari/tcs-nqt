# https://takeuforward.org/arrays/print-fibonacci-series-up-to-nth-term/


# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)
i1 = 0
i2 = 1
n = 5

print(i1)
print(i2)

while i2 < n:
    i3 = i1 + i2
    print(i3)
    i1 = i2
    i2 = i3