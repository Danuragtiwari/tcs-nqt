#https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/
# Example 1:
# Input:153 
# Output: Yes, it is an Armstrong Number
# Explanation: 1^3 + 5^3 + 3^3 = 153

# Input:170 
# Output: No, it is not an Armstrong Number
# Explanation: 1^3 + 7^3 + 0^3 != 170
n=153
# n=170 
check=0
for i in str(n):
    check+=int(i)**len(str(n))
if int(check)==n: print(True) 
else:print(False)