# https://takeuforward.org/data-structure/convert-binary-to-decimal/

# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.
n=1011
ans=0
power=0
for i in str(n)[::-1]:
    if i=='1':
        ans+=2**power 
    power+=1 
print(ans)
        
        

















