# https://takeuforward.org/data-structure/program-to-find-roots-of-a-quadratic-equation/


# Example 1:
# Input: a = 1, b = -3, c = -10
# Output: Roots are real and different, i.e(5 , -2).

import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        # Two real and different roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return "Roots are real and different, i.e. ({:.2f}, {:.2f})".format(root1, root2)
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return "Roots are real and same, i.e. {:.2f}".format(root)
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return "Roots are complex, i.e. ({:.2f} + {:.2f}i, {:.2f} - {:.2f}i)".format(real_part, imaginary_part, real_part, imaginary_part)

# Input coefficients
a = 1
b = -3
c = -10

# Find and print the roots
result = find_roots(a, b, c)
print(result)