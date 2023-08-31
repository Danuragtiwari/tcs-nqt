# https://takeuforward.org/data-structure/permutations-in-which-n-people-can-occupy-r-seats/



# Example 1:
# Input: N = 5, r = 3
# Output: 60


import math

def calculate_permutations(n, r):
    if n < r:
        return 0  # It's not possible to permute more people than available.

    permutations = math.factorial(n) // math.factorial(n - r)
    return permutations

# Example usage:
n = 5
r = 3
result = calculate_permutations(n, r)
print(result)