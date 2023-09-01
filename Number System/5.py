# https://takeuforward.org/data-structure/convert-octal-to-binary/



# Example 1:
# Input: 345
# Output: 011100101
# Explanation: Binary equivalent of given Octal expressionis 011100101

n=345 
deci=int(str(n),8)
# print(type(deci))
print(bin(deci)[2:])