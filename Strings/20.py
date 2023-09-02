# https://takeuforward.org/data-structure/change-every-letter-with-next-lexicographic-alphabet/

# Example 1:
# Input: string str = “abcdxyz”
# Output: bcdeyza

#  a program to change every letter in the given string with the letter following it in the alphabet (ie. a becomes b, p becomes q, z becomes a)
st='abcdxyz'
ans=''
for i in st:
    if i=='z':
        ans+='a'
       
    elif i.isalpha():
        char=chr(ord(i)+1)
      
        ans+=char  
print(ans)