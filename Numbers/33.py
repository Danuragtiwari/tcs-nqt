# # https://takeuforward.org/data-structure/express-given-number-as-sum-of-two-prime-numbers/


# Example 1:
# Input : N = 74
# Output : True . 
# Explanation: 74 can be expressed as 71 + 3 and both are prime numbers.

class SumOf2Prime:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_sum_of_primes(self, n):
        if n <= 2:
            return False
        
        for i in range(2, n // 2 + 1):
            if self.is_prime(i) and self.is_prime(n - i):
                return True
        
        return False

n = 19
s1 = SumOf2Prime()
if s1.is_sum_of_primes(n):
    print("Yes")
else:
    print("No")

            