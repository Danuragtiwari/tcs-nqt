# https://takeuforward.org/data-structure/sum-of-the-numbers-in-a-string/


# Example 1:
# Input: string = “123xyz”
# Output: 123

# Example 2:
# Input: string = “1xyz23”
# Output: 24

s='123xyz'
ans=0
for i in s:
    if i.isnumeric():
        ans+=int(i)
print(ans)